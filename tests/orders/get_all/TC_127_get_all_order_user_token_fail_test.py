import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify no orders returns with user token")
def test_no_orders_return_user_token():
    order_api = Api("order/get-all")
    result = order_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
