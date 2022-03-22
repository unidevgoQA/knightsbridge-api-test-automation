from utils.read_update_counter import read_counter
import datetime

from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('promotion/get-all?promoType=banner')
result = api.get_request(headers=admin_headers_with_token)
random_promotion_id = choice(result['response']['data'])['_id']


counter_reading = read_counter()

now_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# new_promotion_data = {
#   "id": "testpromotion{}".format(counter_reading),
#   "title": "Test Promotion {}".format(counter_reading),
#   "description": "Test Description {}".format(counter_reading),
#   "image": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
#   "startDate": "{}".format(now_date),
#   "expiryDate": "2025-12-10T08:34:22.084Z",
#   "promoType": "banner",
#   "discountPercentage": "5",
#   "coinId": "61b1d3ae18ec7f2e0be3980c",
# }
new_promotion_data = {
  "id": "testpromotion121212121",
  "title": "Test Promotion {}".format(counter_reading),
  "description": "Test Description {}".format(counter_reading),
  "image": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
  "startDate": "{}".format(now_date),
  "expiryDate": "2025-12-10T08:34:22.084Z",
  "promoType": "banner",
  "discountPercentage": "5",
  "coinId": "61b1d3ae18ec7f2e0be3980c",
}

promo_type_data = {
  "static": "static",
  "banner": "banner"
}

coin_id = "61b1d3ae18ec7f2e0be3980c"
promotion_id = '61af47bc32a5660023e80dea'

promotion_to_update ={
  "id": "61b314e4f62c7d0023c96753",
  "title": "Test Promotion updated {}".format(counter_reading),
  "description": "Test Description updated {}".format(counter_reading),
  "image": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
  "startDate": "{}".format(now_date),
  "expiryDate": "2025-12-10T08:34:22.084Z",
  "promoType": "static",
  "discountPercentage": "6",
  "coinId": "61b1d3ae18ec7f2e0be3980c",
}