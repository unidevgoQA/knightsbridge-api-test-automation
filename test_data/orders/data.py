from utils.read_update_counter import read_counter

new_order_data = {
    "uid": "testuid{}".format(read_counter()),
    "coinId": "61b1d3ae18ec7f2e0be3980c",
    "quantity": 2,
    "desiredRate": 2,
    "fee": 1,
    "type": "BUY"
}

order_get_data = {
    "uid": "testuid{}".format(read_counter()),
    "coinId": "61b1d3ae18ec7f2e0be3980c",
}

order_get_data_invalid_uid = {
    "uid": "testuidasdf34",
    "coinId": "61b1d3ae18ec7f2e0be3980c",
}

order_get_data_invalid_coin_id = {
    "uid": "testuidasdf34",
    "coinId": "61b1d3ae18ec7f2ssde0be3980c",
}

get_all_orders_data = {
    "pageSize": "1",
    "pageNumber": "1",
}

user_id = "6196b1eb973d8bd3a40ec126"
user_id_invalid = "6196b1eb973d8bd3a40ec12"

order_status = {
  "status": "In Review"
}

approve_data = {
  "fee": 1,
  "quantity": 2,
  "unitCoinPrice": 3
}

order_id = '61b33ea410c10f0027c5e829'
