import argparse
import json
import sys
from configparser import ConfigParser
from urllib import parse, request, error


BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def _get_api_key():
  #fetching the api kety  from the configuration file 

  config = ConfigParser()
  config.read('secrets.ini')
  return config['openweather']['api_key']



def read_user_cli_args():
  
#handles CLI interactions 

  parser = argparse.ArgumentParser(
    description = 'gets weather and temperature       for a city'
      )
  parser.add_argument(
    'city', nargs= '+', type= str, help='enter the city name'
  )
  parser.add_argument(
    '-i',
    '--imperial',
    action='store_true',
    help='display the temperature in imperial units'
  )
  parser
  return parser.parse_args()

def build_weather_query(city_input, imperial=False):
  
  # "Builds the URL for an API request to OpenWeather's weather API."

  api_key = _get_api_key()
  city_name = ''.join(city_input)
  url_encoded_city_name = parse.quote_plus(city_name)
  units = 'imperial' if imperial else 'metric'
  url = (
    f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
    f"&units={units}&appid={api_key}"
  )
  return url


def get_weather_data(query_url):
   # """Makes an API request to a URL and returns the data as a Python object.

    # Args:
    #     query_url (str): URL formatted for OpenWeather's city name endpoint

    # Returns:
    #     dict: Weather information for a specific city
  try:
    response = request.urlopen(query_url)
  except error.HTTPError as http_error:
    if http_error.code == 401:
      sys.ext('access denied. check api key')
    elif http_error.code == 404:
      sys.exit('Cant find weather data for this city')
    else:
      sys.ext(f'Something went wrong...({http_error.code}) ')
    sys.exti('Cant find weather data for this city')
  data = response.read()

  try:
    return json.loads(data)
  except json.JSONDecodeError:
    sys.exit('couldnt read the servers response')


def display_weather_info(weather_data, imperial=False):
  # prints formateed weather city info
  # arg:  weather_data and imperial

  city = weather_data['name']
  weather_description = weather_data['weather'][0]['description']
  temperature = weather_data['main']['temp']

  
  print(f"{city}", end="")
  print(f"\t{weather_description.capitalize()}", end=" ")
  print(f"({temperature}°{'F' if imperial else 'C'})")
  
if __name__ == "__main__":
  user_args = read_user_cli_args()
  query_url = build_weather_query(user_args.city, 
  user_args.imperial)
  weather_data = get_weather_data(query_url)
  # display_weather_info(weather_data, user_args.imperial)

