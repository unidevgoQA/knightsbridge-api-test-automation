import allure
from api.common_api import Api
from test_data.orders.data import order_get_data_invalid_coin_id
from test_data.headers import headers_with_token


@allure.step("Verify that the order is not retrieved with invalid coin id")
def test_retrieve_order_invalid_coin_id():
    order_api = Api("order/get")
    result = order_api.post_request(order_get_data_invalid_coin_id, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404  # failing because of insufficient balance could not place order
