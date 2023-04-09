from os import environ, path
from dotenv import load_dotenv

load_dotenv()
if environ.get('PASSWORD_MANAGER_DEFAULT_USERNAME') is None:
    with open(f'{path.dirname(__file__)}\\.env', 'w') as file:
        username = input('Username to use by default in future (asked only once!): ')
        environ.setdefault('PASSWORD_MANAGER_DEFAULT_USERNAME', username)
        file.write(f'PASSWORD_MANAGER_DEFAULT_USERNAME={username}')

DEFAULT_USERNAME = environ.get('PASSWORD_MANAGER_DEFAULT_USERNAME')
OUTPUT_FILENAME = f'{path.dirname(__file__)}\\data.json'
