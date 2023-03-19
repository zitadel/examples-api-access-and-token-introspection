import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

ZITADEL_DOMAIN = os.getenv("ZITADEL_DOMAIN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ZITADEL_TOKEN_URL = os.getenv("ZITADEL_TOKEN_URL")
PROJECT_ID = os.getenv("PROJECT_ID")

# Encode the client ID and client secret in Base64
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}".encode("utf-8")
base64_client_credentials = base64.b64encode(client_credentials).decode("utf-8")

# Request an OAuth token from ZITADEL
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {base64_client_credentials}"
}

data = {
    "grant_type": "client_credentials",
    "scope": f"openid profile email urn:zitadel:iam:org:project:id:{PROJECT_ID}:aud read:messages"

}

response = requests.post(ZITADEL_TOKEN_URL, headers=headers, data=data)

if response.status_code == 200:
    access_token = response.json()["access_token"]
    print(f"Response: {response.json()}")
    print(f"Access token: {access_token}")
else:
    print(f"Error: {response.status_code} - {response.text}")
