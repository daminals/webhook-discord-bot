# req.py
# Daniel Kogan
# 02.20.2023

import requests, os
from dotenv import load_dotenv

load_dotenv()
SERVER_URL = os.environ["SERVER_URL"] # your server url goes here

def ping_server(message):
  json_message =  {"message": message } 
  requests.post(SERVER_URL, json=json_message)

ping_server("Hello ur mother!")