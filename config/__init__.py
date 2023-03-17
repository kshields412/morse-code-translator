import configparser

config = configparser.ConfigParser()

config.read('config.ini')

windows_host = config['windows']['host']
windows_user = config['windows']['user']
windows_password = config['windows']['password']

linux_host = config['linux']['host']
linux_user = config['linux']['user']
linux_password = config['linux']['password']
