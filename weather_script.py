import requests

def fetch_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        weather_data = response.json()

        # Extract and display relevant information
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    api_key = "99e64581f2a4fec074366e8653a14d5d"
    city_name = input("Enter the city name: ")
    fetch_weather(city_name, api_key)