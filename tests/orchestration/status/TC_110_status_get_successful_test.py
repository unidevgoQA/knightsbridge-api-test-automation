import allure
from api.common_api import Api


@allure.step("Verify user can get status")
def test_status_api_loads():
    status_api = Api("status")
    result = status_api.get_request_status()
    status_code = result.status_code
    assert status_code == 200
