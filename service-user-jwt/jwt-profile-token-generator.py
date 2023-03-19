import json
import time
import requests
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

ZITADEL_DOMAIN = os.getenv("ZITADEL_DOMAIN")
CLIENT_PRIVATE_KEY_FILE_PATH = os.getenv("CLIENT_PRIVATE_KEY_FILE_PATH")
ZITADEL_TOKEN_URL = os.getenv("ZITADEL_TOKEN_URL")
PROJECT_ID = os.getenv("PROJECT_ID")

# Load the downloaded JSON file
with open(CLIENT_PRIVATE_KEY_FILE_PATH, "r") as f:
    json_data = json.load(f)

private_key = json_data["key"]
kid = json_data["keyId"]
user_id = json_data["userId"]

# Create JWT header and payload
header = {
    "alg": "RS256",
    "kid": kid
}

payload = {
    "iss": user_id,
    "sub": user_id,
    "aud": ZITADEL_DOMAIN,
    "iat": int(time.time()),
    "exp": int(time.time()) + 3600
}

# Sign the JWT
jwt_token = jwt.encode(payload, private_key, algorithm='RS256', headers=header)

# Request an OAuth token from ZITADEL
data = {
    "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "scope": f"openid profile email urn:zitadel:iam:org:project:id:{PROJECT_ID}:aud read:messages",
    "assertion": jwt_token
}

response = requests.post(ZITADEL_TOKEN_URL, data=data)

if response.status_code == 200:
    access_token = response.json()["access_token"]
    print(f"Response: {response.json()}")
    print(f"Access token: {access_token}")
else:
    print(f"Error: {response.status_code} - {response.text}")
