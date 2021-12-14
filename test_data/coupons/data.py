from utils.read_update_counter import read_counter

new_coupon = {
  "discountPercentage": 0,
  "title": "Test Coupon",
  "startDate": "2019-09-07",
  "endDate": "2020-09-07",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}

create_invalid_coupon = {
  "discountPercentage": 0,
  "title": "",
  "startDate": "12 Dec 2021",
  "endDate": "20 Dec 2021",
  "forAllCoins": True,
  "coinId": "111",
  "image": "https://www.cryptocompare.com/media/12318076/xrp.png",
  "code": "TC111",
  "noOfReedem": 0
}




coupon_type = "testType"
coupon_id = "61b1d3de18ec7f2e0be39810"
invalid_coupon_id = "sdfadfaertersazdg"
coupon_id_to_update = "61b1d3ae18ec7f2e0be3980c"

coupon_get_all_params = {
  "pageSize": "1",
  "pageNumber": "12",
  "search": "Test coupon"
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
  "startDate": "7 Dec 2021",
  "endDate": "15 Dec 2021",
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
