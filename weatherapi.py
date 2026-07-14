import requests

api_key= "28c872cdbd395f6142d4e226adc70d48"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n------ Weather Report ------")
    print(f"City        : {city_name}, {country}")
    print(f"Temperature : {temperature}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Condition   : {weather.title()}")
    print(f"Wind Speed  : {wind_speed} m/s")

else:
    print("Invalid city name or API request failed.")