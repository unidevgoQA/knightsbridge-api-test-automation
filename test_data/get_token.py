import requests
import json
from api.user_api import UserApi
from test_data.user_data.data import valid_user_data
from test_data.admin.data import admin_credentials
from api.config import constData


def get_token():
    url = constData['BASE_API_URL'] + 'api/users/signin'
    payload = json.dumps({"email": "ss.unidev@gmail.com", "password": "5946644Ss@"})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    body = response.json()
    token = body['token']
    return token


def get_admin_token():
    """
    Returns the admin token
    """
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(admin_credentials)
    user_id = result['response']['id']
    token = result['response']['token']
    return user_id, token


user_token = get_token()
admin_token = get_admin_token()[1]
admin_id = get_admin_token()[0]

