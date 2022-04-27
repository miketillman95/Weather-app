import argparse
from configparser import ConfigParser


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

if __name__ == "__main__":
  read_user_cli_args()