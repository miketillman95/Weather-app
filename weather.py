import argparse
from configparser import ConfigParser
from urllib import parse


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
  
  "Builds the URL for an API request to OpenWeather's weather API."

  api_key = _get_api_key()
  city_name = ''.join(city_input)
  url_encoded_city_name = parse.quote_plus(city_name)
  units = 'imperial' if imperial else 'metric'
  url = (
    f"{BASE_WEATHER_API_URL}?q{url_encoded_city_name}"
    f"&units={units}&appid={api_key}"
  )
  return url
    

if __name__ == "__main__":
  user_args = read_user_cli_args()
  query_url = build_weather_query(user_args.city, user_args.imperial)
  print(query_url)