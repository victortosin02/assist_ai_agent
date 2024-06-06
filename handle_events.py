import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')

def handle_event(event):
    if event['type'] == 'tracker_response':
        for tracker in event['trackers']:
            print(f"Tracker: {tracker['name']}")
            for match in tracker['matches']:
                print(f"Matched text: {match['value']}")

def fetch_events(conversation_id):
    url = f"https://api.symbl.ai/v1/conversations/{conversation_id}/events"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        events = response.json()['events']
        for event in events:
            handle_event(event)
    else:
        print(f"Failed to retrieve events: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    conversation_id = "4960927899320320"
    fetch_events(conversation_id)
