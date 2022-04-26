from configparser import ConfigParser


def _get_api_key():
  #fetching the api kety  from the configuration file 

  config = ConfigParser()
  config.read('secrets.ini')
  return config['openweather']['api_key']


import argparse
from configparser import ConfigParser

def read_user_cli_args():
  
#handles CLI interactions 

  parser = argparse.ArgumentParser(
    description = 'gets weather and temperature       for a city'
      )
  return parser.parse_args()

if __name__== '_main_':
  read_user_cli_args()