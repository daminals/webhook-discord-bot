# server.py
# Daniel Kogan
# 12.27.2022

import requests, os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

WEBHOOK_URL = os.environ["WEBHOOK_URL"] # your webhook url goes here

def send_message_to_discord(message):
  data = {
    "content": message
  }
  requests.post(WEBHOOK_URL, json=data)  


@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/discord', methods=['POST'])
def discord():
    data = request.get_json()
    send_message_to_discord(data["message"])
    return 'Message sent!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')