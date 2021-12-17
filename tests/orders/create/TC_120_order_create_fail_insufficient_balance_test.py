import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.orders.data import new_order_data


@allure.step("Verify order creates unsuccessful with insufficient balance")
def test_order_create_insufficient_wallet():
    order_api = Api("order/create")
    result = order_api.post_request(new_order_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 422
