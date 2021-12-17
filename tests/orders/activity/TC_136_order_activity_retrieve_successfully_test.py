import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token


@allure.step("Validate retrieve order successfully")
def test_approve_order_no_token():
    api_endpoint = "order/activity?pageSize=1&pageNumber=1"
    order_api = Api(api_endpoint)
    result = order_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
