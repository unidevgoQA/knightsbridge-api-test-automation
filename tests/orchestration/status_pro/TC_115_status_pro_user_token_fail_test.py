import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify user can not get status pro")
def test_status_pro_not_loads():
    status_api = Api("status/pro")
    result = status_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
