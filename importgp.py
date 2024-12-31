#!/usr/bin/env python3

import os
import json
import requests
import getpass
import base64
from datetime import datetime

url = input("Enter the url: ")
username = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")

# get nfl sportsbook data
def get_nfl_info():
    response = requests.get)(f"{base_url}")
    return response.json()

# function to write data to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

data = {
    'NFL information': get_nfl_info()
}

# Get the current date and time