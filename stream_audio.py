import os
from dotenv import load_dotenv
import symbl

# Load environment variables from .env file
load_dotenv()

app_id = os.getenv('APP_ID')
app_secret = os.getenv('APP_SECRET')

async def start_streaming():
    try:
        symbl = symbl(appId=app_id, appSecret=app_secret)
        connection = await symbl.createAndStartNewConnection()

        connection.on('speech_recognition', lambda speech_data: {
            'name': speech_data.user.name if speech_data.user else 'User',
            'transcript': speech_data.punctuated.transcript
        })

        await symbl.wait(60000)
        await connection.stopProcessing()
        connection.disconnect()
    except Exception as e:
        print(f"Error in start_streaming: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_streaming())
