import allure
from api.common_api import Api


@allure.step("Verify user can not get status with post request")
def test_status_api_not_loads_post():
    status_api = Api("status")
    result = status_api.post_request()
    status_code = result['status_code']
    assert status_code == 404
