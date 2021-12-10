from utils.read_update_counter import read_counter

new_order_data = {
  "uid": "testuid{}".format(read_counter()),
  "coinId": "61b1d3ae18ec7f2e0be3980c",
  "quantity": 2,
  "desiredRate": 2,
  "fee": 1,
  "type": "BUY"
}

