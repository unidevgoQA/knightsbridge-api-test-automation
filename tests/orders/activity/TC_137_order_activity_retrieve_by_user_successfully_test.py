import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Validate retrieve order fail")
def test_approve_order_user():
    api_endpoint = "order/activity?pageSize=1&pageNumber=1"
    order_api = Api(api_endpoint)
    result = order_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
