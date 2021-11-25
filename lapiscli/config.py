import configparser
import os
import sys
# the config file path is ~/.lapis/config.conf
config_file = os.path.expanduser('~/.lapis/config.conf')

defaults = {
    'host': 'localhost',

}