from random import choice
from utils.read_update_counter import read_counter
from api.common_api import Api
from test_data.headers import admin_headers_with_token

counter_reading = read_counter()

api = Api('bank/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_bank = choice(result['response']['data'])
random_bank_id = random_bank['_id']
random_bank_user_id = random_bank['userId']

new_bank = {
  "userId": "test123",
  "bankName": "test bank",
  "title": "test bank",
  "country": "bd",
  "swiftCode": "3243s",
  "accountNumber": "3453464564756765"
}

bank_id = "61996e25f613eb001c2258c0"
bank_id_to_delete = "61996e25f613eb001c2258c2"
invalid_bank_id = "61996e25f613easdf34fsdf"

updated_bank_data = {
  "bankName": "updated test bank",
  "title": "Update bank",
  "country": "bd",
  "accountNumber": "4645756745645765"
}
