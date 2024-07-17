import requests
from keys import WEATHER_API

location=input('Enter the location name\n')

response=requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={location}&aqi=no')

if response.status_code == 200 :
    data=response.json()
    print(f'Location name : {data["location"]["name"]}')
    print(f'Location region : {data["location"]["region"]}')
    print(f'Location country : {data["location"]["country"]}')
    print(f'Location localtime : {data["location"]["localtime"]}')
    print(f'Location is_day : {data["current"]["is_day"]}')
    print(f'Location temperature : {data["current"]["temp_c"]} celsius')
    print(f'Location wind direction : {data["current"]["wind_dir"]}')
    print(f'Location wind speed : {data["current"]["wind_kph"]} kph')
    print(f'Location humidity : {data["current"]["humidity"]}')
    print(f'Location cloud : {data["current"]["cloud"]}')
else:
    print("Invalid location name")