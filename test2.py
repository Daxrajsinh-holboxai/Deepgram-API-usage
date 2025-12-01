import os
import requests
import json
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY = os.getenv("DEEPGRAM_API_KEY")
PROJECT_ID = os.getenv("DEEPGRAM_PROJECT_ID")

if not API_KEY or not PROJECT_ID:
    raise ValueError("Missing DEEPGRAM_API_KEY or DEEPGRAM_PROJECT_ID in .env")

url = f"https://api.deepgram.com/v1/projects/{PROJECT_ID}/usage"

# Note: Change the start and end date accordingly.
params = {
    "start": "2025-10-01",
    "end": "2025-12-31"
}

headers = {
    "Authorization": f"Token {API_KEY}",
    "accept": "application/json"
}

response = requests.get(url, headers=headers, params=params)

print("Status:", response.status_code)
# Pretty-print JSON
try:
    data = response.json()
    print(json.dumps(data, indent=4))
except ValueError:
    print("Response is not valid JSON:")
    print(response.text)
