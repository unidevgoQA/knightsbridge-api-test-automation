from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('coupon/getAll')
result = api.get_request(headers=admin_headers_with_token)
random_coupon_id = choice(result['response']['data'])['_id']

new_coupon = {
  "discountPercentage": 0,
  "title": "Automation",

  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "A1215",
  "noOfReedem": 0
}

create_invalid_coupon = {
  "discountPercentage": 0,
  "title": "",
  "startDate": "2019-09-07",
  "endDate": "2019-10-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}




coupon_type = "testType"
coupon_id = "61b875093542c30024f21b0c"
invalid_coupon_id = "sdfadfadfadfdfertersazdg"
coupon_id_to_update = "61b875093542c30024f21b0c"

coupon_get_all_params = {
  "pageSize": "1",
  "pageNumber": "12",
  "search": "Test coupon"
}


use_new_coupon = {
  "coinId": "111",
  "userId": "string",
  "couponId": "6214d5798c300600230ddbbd",
  "orderId": "dadsfsd",
  "redeemDate": "2020-09-07"
}

coupon_get_by_id = {
  "id": "1"
}

coupon_delete_by_id = {
  "id": "1"
}

coupon_to_search = "Test Coupon"

update_coupon_data = {
  "discountPercentage": 0,
  "title": "Test Coupon",
  "startDate": "2019-09-07",
  "endDate": "2019-10-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_only_title = {
  "title": "Test1 Coupon"
}

coupon_create_only_discountPercentage = {
  "discountPercentage": 10
}

coupon_create_only_startDate = {
  "startDate": "7 Dec 2021"
}

coupon_create_only_endDate = {
  "endDate": "7 Dec 2021"
}

coupon_create_only_forAllCoins = {
  "forAllCoins": True
}

coupon_create_only_coinId = {
  "coinId": "4521"
}

coupon_create_only_image = {
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png"
}

coupon_create_only_code = {
  "code": "4444"
}

coupon_create_only_noOfReedem = {
  "noOfReedem": 10
}

coupon_create_except_discount = {
  "title": "Test3 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_title = {
  "discountPercentage": 10,
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_startDate = {
  "discountPercentage": 10,
  "title": "Test22 Coupon",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_endDate = {
  "discountPercentage": 10,
  "title": "Test31 Coupon",
  "startDate": "2019-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_forAllCoins = {
  "discountPercentage": 10,
  "title": "Test30 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_coinId = {
  "discountPercentage": 10,
  "title": "Test7 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_image = {
  "discountPercentage": 10,
  "title": "Test9 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "code": "TC111",
  "noOfReedem": 0
}

coupon_create_except_code = {
  "discountPercentage": 10,
  "title": "Test8 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "noOfReedem": 0
}

coupon_create_except_noOfReedem = {
  "discountPercentage": 10,
  "title": "Test6 Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111"
}


