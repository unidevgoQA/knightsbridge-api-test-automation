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
