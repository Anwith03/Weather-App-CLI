import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key from .env file
API_KEY = os.getenv("API_KEY")

# Ask user for city name
city = input("Enter city name: ")

# Weather API URL
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

# Send request to WeatherAPI
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check for errors
if "error" in data:
    print("\n❌ Error!")
    print(data["error"]["message"])
else:
    print("\n" + "=" * 45)
    print("            WEATHER REPORT")
    print("=" * 45)

    print(f"City        : {data['location']['name']}")
    print(f"Region      : {data['location']['region']}")
    print(f"Country     : {data['location']['country']}")
    print(f"Temperature : {data['current']['temp_c']} °C")
    print(f"Feels Like  : {data['current']['feelslike_c']} °C")
    print(f"Humidity    : {data['current']['humidity']} %")
    print(f"Wind Speed  : {data['current']['wind_kph']} km/h")
    print(f"Condition   : {data['current']['condition']['text']}")

    print("=" * 45)