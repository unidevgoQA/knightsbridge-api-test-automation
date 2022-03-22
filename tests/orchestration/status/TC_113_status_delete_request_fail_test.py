import allure
from api.common_api import Api


@allure.step("Verify user can not get status with delete request")
def test_status_api_not_loads_delete():
    status_api = Api("status")
    result = status_api.delete_request()
    status_code = result['status_code']
    assert status_code == 404
