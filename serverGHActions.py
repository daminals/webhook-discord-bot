# serverGHActions.py
# Daniel Kogan
# 02.20.2023

import requests, os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

WEBHOOK_URL = os.environ["WEBHOOK_URL"] # your webhook url goes here

def send_message_to_discord(data):
  if not ('action' in data and 'workflow_run' in data):
    return 400 # error, return error code
  if not data['action'] == 'completed':
    return 200 # ignore in progress and requested workflows, throw accepted
  name = data['workflow_run']['name'] # workflow name
  status = data['workflow_run']['conclusion'] # success, failure, cancelled
  repo_name = str(data['repository']['full_name']) # repository name
  if status == 'success': status+=' ✅' 
  else: status+=' ❌'
  data = {
    "content": f"**{repo_name}**: Workflow __{name}__ has completed with status **{status}**"
  }
  requests.post(WEBHOOK_URL, json=data)  
  return 200 # success


@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/discord', methods=['POST'])
def discord():
    data = request.get_json()
    status = send_message_to_discord(data)
    return 'Message sent!', status

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')