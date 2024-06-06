import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')

def get_trackers(conversation_id):
    url = f"https://api.symbl.ai/v1/conversations/{conversation_id}/trackers"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        trackers = response.json()
        print("Trackers:", json.dumps(trackers, indent=2))
        return trackers
    else:
        print(f"Failed to retrieve trackers: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    conversation_id = "4960927899320320"
    get_trackers(conversation_id)
