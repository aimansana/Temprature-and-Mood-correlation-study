from datetime import datetime
import pandas as pd
from meteostat import Point, Daily

def fetch_historical_weather(city_name="London", latitude=51.5072, longitude=-0.1276,
                             start="2022-01-01", end="2022-12-31",
                             filename="data/london_weather.csv"):
    """
    Fetch historical daily weather data (temperature) using Meteostat API.
    Saves it as a CSV file.
    """

    # Define location (city coordinates)
    location = Point(latitude, longitude)

    # Convert start/end into datetime
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")

    # Get daily weather
    data = Daily(location, start_dt, end_dt)
    df = data.fetch()

    # Reset index & keep only temperature columns
    df = df.reset_index()[["time", "tavg", "tmin", "tmax"]]
    df.rename(columns={"time": "date"}, inplace=True)

    # Save to CSV
    df.to_csv(filename, index=False)

    print(f"✅ Saved {len(df)} rows of weather data for {city_name} to {filename}")
    print(df.head())

if __name__ == "__main__":
    fetch_historical_weather(
        city_name="London",
        latitude=51.5072,
        longitude=-0.1276,
        start="2022-01-01",
        end="2022-12-31",
        filename="data/london_weather.csv"
    )
