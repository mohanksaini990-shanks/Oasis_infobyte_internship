import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        print("City not found! Please try again.")
        return
    
    city_name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    
    print(f"\n===== Weather in {city_name}, {country} =====")
    print(f"Temperature : {temp}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Condition   : {condition.capitalize()}")

def main():
    print("===== Basic Weather App =====")
    api_key = "28c872cdbd395f6142d4e226adc70d48" 
    city = input("Enter city name: ")
    get_weather(city, api_key)

main()