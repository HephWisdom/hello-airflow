import requests
import pandas as pd

def extract_weather_data(api_key, city)-> dict:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None



def transform_weather_data(weather_data: dict) -> pd.DataFrame:
    if not weather_data:
        return pd.DataFrame()
    try:
        main_data = weather_data['main']
        weather_data_transformed = {
            'temperature': main_data['temp'],
            'pressure': main_data['pressure'],
            'humidity': main_data['humidity'],
            'city': weather_data['name'],
            'country': weather_data['sys']['country']
        }
        return pd.DataFrame([weather_data_transformed])
    except KeyError as e:
        print(f"Error transforming weather data: {e}")
        return pd.DataFrame()
