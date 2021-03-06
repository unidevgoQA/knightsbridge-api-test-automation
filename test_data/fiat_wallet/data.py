from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('fiatWallet/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_user_id = choice(result['response']['data'])['userId']
random_fiat_wallet_id = choice(result['response']['data'])['_id']

new_fiat_wallet_data = {
  "userId": "0152123997001705569764",
  "fiatAmount": 100,
  "reservedAmount": 50
}

fiat_wallet_id = '61ab37b42868e900116ed83e'

fiat_wallet_update_data = {
  "userId": random_user_id,
  "fiatAmount": 4,
  "reservedAmount": 1
}

# get random wallet user id to get rid of the chance of index out of range
fiat_wallet_user_id = random_user_id