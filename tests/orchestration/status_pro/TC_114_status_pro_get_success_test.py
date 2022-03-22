import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token


@allure.step("Verify user can get status pro successfully")
def test_status_pro_loads():
    status_api = Api("status/pro")
    result = status_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
