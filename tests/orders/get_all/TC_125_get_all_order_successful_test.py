import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token


@allure.step("Verify get all orders")
def test_get_all_orders():
    order_api = Api("order/get-all?pageSize=1&pageNumber=1")
    result = order_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
