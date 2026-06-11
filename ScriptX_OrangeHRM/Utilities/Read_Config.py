from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("Configurations/Config.ini")
    return config.get(category, key)
