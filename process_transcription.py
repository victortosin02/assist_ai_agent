import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')

def get_transcription(conversation_id):
    url = f"https://api.symbl.ai/v1/conversations/{conversation_id}/messages"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = response.json()['messages']
        for message in messages:
            print(f"{message['from']['name']}: {message['text']}")
    else:
        print(f"Failed to retrieve messages: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    conversation_id = "4960927899320320"
    get_transcription(conversation_id)
