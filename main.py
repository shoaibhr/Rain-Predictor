#imports
import requests


api_key = "0f603954f591dcf162d835095eed03b8"
api_url = f"https://api.openweathermap.org/data/2.5/weather?"

api_params = {
    "q": "Lahore, Pakistan",
    "appid": api_key,
    "units": "metric"
}

api_data = requests.get(api_url, params=api_params).json()
print(api_data["main"]["temp"])

