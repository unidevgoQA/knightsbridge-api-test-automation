from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

# Get random wallet id
api = Api('adminWallet/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_wallet_id = choice(result['response']['data'])['_id']

# get a random coinId
# coin_type_endpoint = "coin/get-all?isActive=true&coinType=testType"
# coin_api = Api(coin_type_endpoint)
# result = coin_api.get_request(headers=admin_headers_with_token)
# random_coin_id = choice(result['response']['data'])['_id']

new_admin_wallet = {
  "logo": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
  "walletName": "TESTWallet",
  "walletAddress": "testAddress",
  "coinId": "testType"
}

wallet_id_invalid = "skdjfaslkdfjw45jl34kj5"