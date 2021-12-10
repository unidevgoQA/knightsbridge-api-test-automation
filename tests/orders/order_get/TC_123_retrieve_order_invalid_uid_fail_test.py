import allure
from api.common_api import Api
from test_data.orders.data import order_get_data_invalid_uid
from test_data.headers import headers_with_token


@allure.step("Verify that the order is not retrieved with invalid uid")
def test_retrieve_order_invalid_uid():
    order_api = Api("order/get")
    result = order_api.post_request(order_get_data_invalid_uid, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404  # failing because of insufficient balance could not place order
