import requests

def get_weather(city, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(api_url, params=api_params)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        api_data = response.json()
        
        # Check if 'main' and 'temp' are in the response
        if "main" in api_data and "temp" in api_data["main"]:
            return api_data["main"]["temp"]
        else:
            print("Error: Unexpected response structure.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Example usage
api_key = ""  # Consider using environment variables
city = "Lahore, Pakistan"
temperature = get_weather(city, api_key)

if temperature is not None:
    print(f"The temperature in {city} is {temperature}°C.")
