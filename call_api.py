import json
import requests
from dotenv import load_dotenv
import os

"""
In this DEMO , you might face error when import package from dotenv
To resolve it, You should do 2~3 things first

1. add an virtual environment (venv)  : this is optional, it depends on your environment setting
2. add 'python-dotenv' on the 'requirements.txt' file
3. Input the command 'pip install -r ./requirements.txt' on you terminal
"""

def get_weather_by_coordinates():
    """
    Description:     
        Use the API provided by openweather to demo how to call API in Python
        API Server: openweathermap
        API Doc: https://openweathermap.org/current#name
        You have to create a key from openweathermap website first for accessing the API 
    
    """
    # Load api_key fron .env file first
    load_dotenv()
    api_key = os.getenv('weather_api_key')

    lat = str(25)
    lon = str(121)
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(lat,lon, api_key)
    response = requests.get(url)
    return response.json()

weather_json = get_weather_by_coordinates()

"""
    Either one can display the json result from the API
"""
#print(weather_json)
print(json.dumps(weather_json))
print()
print(f"the temparature is {weather_json['main']['temp']}")
print()
print(f"the weather is {weather_json['weather'][0]['main']}")
print()

