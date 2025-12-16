# 🌧️ Rain Alert

A Python automation script that checks the weather forecast and sends an SMS alert if rain is expected for the day.

## ✨ Technologies

- `Python`
- `Requests`
- `API`
- `Twilio`
- `Environment Variables`

## 🚀 Features

- Fetches weather forecast data from OpenWeatherMap
- Checks upcoming weather conditions for rain
- Sends SMS alerts using Twilio
- Secure handling of API keys using environment variables
- Designed to run automatically on a schedule

## 📍 The Process

This project was built as **Day 35 of the 100 Days of Python Code** course.

The focus was on learning how to securely handle sensitive information using environment variables instead of hardcoding API keys and credentials. The `os.environ.get()` method was used to access these values at runtime while keeping them out of version control.

The project uses the OpenWeatherMap API to fetch weather data for a specified location and analyzes weather condition codes to determine if rain is expected. If rain is detected, the script sends an SMS notification using the Twilio API.

To make the automation practical, the script was deployed on **PythonAnywhere**, where it runs daily in the morning and notifies the user in advance if rain is expected.

## 🚦 Running the Project

1. Clone the repository  
2. Set required environment variables:
   - `OWM_API_KEY`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`
   - `VERIFIED_PHONE_NUMBER`
3. Install dependencies: `pip install requests twilio`
4. Run the script: `python main.py`
5. (Optional) Deploy to a cloud service for scheduled execution
