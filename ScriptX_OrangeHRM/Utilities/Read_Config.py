import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini')
print("Config path:", os.path.abspath(config_path))     
config.read(config_path)
print("Sections found:", config.sections())              

def get_config(category, key):
    return config.get(category, key)