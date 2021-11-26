import configparser
import os
import sys
# the config file path is ~/.lapis/config.conf
config_file = os.path.expanduser('~/.lapis/config.conf')

defaults = {
    'host': 'https://lapis.ultramarine-linux.org/api/',

}

# if config file does not exist, create it at ~/.lapis/config.conf
if not os.path.exists(config_file):
    config = configparser.ConfigParser(defaults)
    # write the config file
    with open(config_file, 'w') as f:
        config.write(f)


def get(key):
    config = configparser.ConfigParser(defaults)
    config.read(config_file)
    return config.get('DEFAULT', key)