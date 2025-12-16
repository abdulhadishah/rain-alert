import requests
from twilio.rest import Client
import os


owm_endpoint = "YOUR_OWM_ENDPOINT"
api_key = os.environ["OWM_API_KEY"]

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_phone = os.environ["TWILIO_PHONE_NUMBER"]
your_verified_no = os.environ["VERIFIED_PHONE_NUMBER"]

LATITUDE = 0.0 #replace with your latitude
LONGITUDE = 0.0  # replace with your longitude

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()

data = response.json()

will_rain = False
city_weather_ids = [dictionaries["weather"][0]["id"] for dictionaries in data["list"]]
for weather_code in city_weather_ids:
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=twilio_phone,
        to=your_verified_no,
    )
    print(message.status)
