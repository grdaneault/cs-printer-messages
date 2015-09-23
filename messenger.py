#!/usr/bin/python3

import sys
from ConfigParser import ConfigParser

config_file = sys.argv[1] if len(sys.argv) >= 2 else "configuration.json"
config = ConfigParser(config_file)

seconds = 0
while True:
    for message in config.get_messages():
        screen = message.screen()
        screen.show(config.get_target_list(), verbose=config.is_verbose())

    config.update_config()
