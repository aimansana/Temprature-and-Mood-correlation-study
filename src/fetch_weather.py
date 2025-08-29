#fetch_weather.py in fetch-weather branch
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_temperature(city="Bengaluru"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data["main"]["temp"]

print("Bengaluru Temp:", get_temperature("Bengaluru"), "°C")

print("Fetching weather data...")

