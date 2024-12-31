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

