import allure
from api.common_api import Api
from test_data.orders.data import order_get_data
from test_data.headers import headers_with_token


@allure.step("Verify that user can retrieve order successfully")
def test_retrieve_order():
    order_api = Api("order/get")
    result = order_api.post_request(order_get_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200  # failing because of insufficient balance could not place order
