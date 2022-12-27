#used to help import the python package for design on the heading
from pyfiglet import Figlet

figlet = Figlet (font = 'slant')


from dotenv import load_dotenv
#used to locate the path of the .env file 
import os

load_dotenv()

#used to help convert the date and time in to more readeable date for the end-user
import datetime as dt

#used to locate or get a request that has been sent to the specific website
import requests

#used to get the information from the specific website 
Base_url = "http://api.openweathermap.org/data/2.5/weather?"

Api_key = os.getenv("Api_keys")

print(figlet.renderText("Welcome to Simon's Weather Station"))


#used to get the user location
City = input('Enter the name of your city >> ').upper()

#used to convert the temperature to a specific degree
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

#used to join the web link with the city of the end-user
url = Base_url + "appid=" + Api_key + "&q=" + City

#used to retrive all the data from the website
response = requests.get(url).json()


#used to locate the information in the dictionary (Temperature and Wind Speed)
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenhiet = kelvin_to_celsius_fahrenheit(temp_kelvin)
wind_speed = response['wind']['speed']
visibility = response['visibility']

#used to locate the information in the dictionary (Feels like temperature)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

#used to locate the information in the dictionary (Humidity temperature)
humidity = response['main']['humidity']
humidity_description = response['weather'][0]['description']


#used to locate the information in the dictionary (Sunset and Sunrise time on the city)
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

#used to get the counrty of the city
country = response['sys']['country']


print(f'City : {City}')
print(f'Country : {country}')
print(f'Temperature in {City} is: {temp_celsius:.2f} or {temp_fahrenhiet:.2f}')
print(f'Temperature in {City} feels like: {feels_like_celsius:.2f} or {feels_like_fahrenheit:.2f}')
print(f'Humidity in {City}: {humidity}%')
print(f'General Weather in {City}: {humidity_description}')
print(f'Wind Sepeed in {City}: {wind_speed}km')
print(f'Visibility in {City} {visibility} meters')
print(f'Sun Rise in {City} at {sunrise_time} local time')
print(f'Sun Sets in {City} at {sunset_time} local time')
