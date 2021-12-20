from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from utils.read_update_counter import read_counter

counter_reading = read_counter()

api = Api('coin/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_coin_id = choice(result['response']['data'])['_id']

new_coin = {
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "realName": "test coin {}".format(read_counter()),
  "title": "test coin",
  "price": 12,
  "exchangeName": "test exchange",
  "description": "good coin",
  "isActive": True,
  "key": "testkey",
  "coinType": "testType"
}

coin_type = "testType"
coin_id = "61b1d3de18ec7f2e0be39810"
invalid_coin_id = "sdfadfaertersazdg"
coin_id_to_update = "61b1d3ae18ec7f2e0be3980c"

coins_get_all_params = {
  "coinType": "coinMarket",
  "isActive": "false"
}

coins_no_type = {
  "coinType": "",
  "isActive": True
}

coins_get_no_is_active = {
  "coinType": "testType",
  "isActive": ""
}

coin_to_search = "Tron"

update_coin_data = {
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "realName": "test coin 2",
  "title": "test coin updated",
  "price": 14,
  "exchangeName": "test exchange updated",
  "description": "good coin updated",
  "isActive": True,
  "key": "testkeyupdated",
  "coinType": "coinMarket"
}