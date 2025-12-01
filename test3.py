import requests, os
from dotenv import load_dotenv

load_dotenv()

resp = requests.get(
    "https://api.deepgram.com/v1/projects",
    headers={"Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}"}
)

print(resp.status_code, resp.text)
