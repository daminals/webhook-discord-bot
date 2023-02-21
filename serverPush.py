# serverPush.py
# Daniel Kogan
# 02.20.2023

# server.py
# Daniel Kogan
# 12.27.2022

import requests, os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

WEBHOOK_URL = os.environ["WEBHOOK_URL"] # your webhook url goes here

def send_message_from_github(data):
  repo_name = str(data['repository']['full_name']) # repository name
  time = str(data['repository']['updated_at']) # time of latest commit
  sender = str(data['pusher']['name']) # who committed
  commit_message = str(data['commits'][0]['message']) # commit message
  data = {
    "content": "A new commit '***"+commit_message+"***' was pushed to *__" + repo_name + "__* by *" + sender + "* at " + time
  }
  requests.post(WEBHOOK_URL, json=data)  

@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/discord', methods=['POST'])
def discord():
    data = request.get_json()
    send_message_from_github(data)
    return 'Message sent!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')