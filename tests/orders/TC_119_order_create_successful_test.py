import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify order creates successful")
def test_order_create():
    order_api = Api("order/create")
    result = order_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
