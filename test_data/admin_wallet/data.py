from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('adminWallet/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_wallet_id = choice(result['response']['data'])['_id']

new_admin_wallet = {
  "logo": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
  "walletName": "TESTWallet",
  "walletAddress": "testAddress",
  "coinId": "61b1d3de18ec7f2e0be39810"
}