import requests
import json
from api.config import constData


def get_token():
    url = constData['BASE_API_URL'] + 'api/users/signin'
    payload = json.dumps({"email": "ss.unidev@gmail.com", "password": "5946644Ss@"})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    body = response.json()
    token = body['token']
    return token


token = get_token()