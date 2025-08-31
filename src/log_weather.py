import os
import requests
import csv
from datetime import datetime
from dotenv import load_dotenv
#aiman
# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_temperature(city="Bengaluru"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if "main" in data:
        return data["main"]["temp"]
    else:
        print("Error:", data)  # Debugging in case API fails
        return None

def log_temperature(city="Bengaluru", filename="data/weather_log.csv"):
    # Make sure the data folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    temp = get_temperature(city)
    if temp is None:
        return

    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write to CSV (append mode)
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "city", "temperature"])  # header row
        writer.writerow([today, city, temp])

    print(f"Logged: {today}, {city}, {temp}°C")

if __name__ == "__main__":
    log_temperature("Bengaluru")
