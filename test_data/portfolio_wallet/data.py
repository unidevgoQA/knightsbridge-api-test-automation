from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('cryptoWallet/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_user_id = choice(result['response']['data'])['userId']

user_id_invalid = "4jhkehidfdusghtwkthsohs"

