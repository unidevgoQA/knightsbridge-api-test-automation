from utils.read_update_counter import read_counter
import datetime

counter_reading = read_counter()

now_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

new_promotion_data = {
  "id": "testpromotion{}".format(counter_reading),
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