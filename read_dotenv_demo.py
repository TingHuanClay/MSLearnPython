from dotenv import load_dotenv
import os

"""
In this DEMO , you might face error when import package from dotenv
To resolve it, You should do 2~3 things first

1. add an virtual environment (venv)
2. add 'python-dotenv' on the 'requirements.txt' file
3. Input the command 'pip install -r ./requirements.txt' on you terminal
"""
load_dotenv()
weather_api_key = os.getenv('weather_api_key')
print(f"weather_api_key: {weather_api_key}")