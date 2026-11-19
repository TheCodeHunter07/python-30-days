# ASSIGNMENT
# 2 weather.py — fetch current weather for a city from open-meteo.com (no API key needed)


import requests

city = input("Enter city name: ")

print("Fetching weather for:", city)

try:

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params)

    data = response.json()

    results = data.get("results")

    if not results:
        print("City not found!")
        exit()

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "timezone": "auto",
        "latitude": data["results"][0]["latitude"],
        "longitude": data["results"][0]["longitude"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    weather_response = requests.get(weather_url, params=weather_params)

    weather_data = weather_response.json()

    print(weather_data)



    print(f"\nWeather Report for {city.title()}")
    print("Temperature:", weather_data["current"]["temperature_2m"], "°C")
    print("Humidity:", weather_data["current"]["relative_humidity_2m"], "%")
    print("Wind Speed:", weather_data["current"]["wind_speed_10m"], "km/h")


except requests.exceptions.Timeout:
    print("Request timed out! Please try again.")

except requests.exceptions.ConnectionError:
    print("No internet connection!")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Something went wrong:", error)