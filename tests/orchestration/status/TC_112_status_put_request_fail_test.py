import allure
from api.common_api import Api


@allure.step("Verify user can not get status with put request")
def test_status_api_not_loads_put():
    status_api = Api("status")
    result = status_api.put_request()
    status_code = result['status_code']
    assert status_code == 404
