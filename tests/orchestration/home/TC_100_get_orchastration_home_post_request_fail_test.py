import allure
from api.common_api import Api


@allure.step("Verify get orchestration post request fail test")
def test_orchestration_home_post():
    promotion_api = Api("")
    result = promotion_api.post_request()
    status_code = result['status_code']
    assert status_code == 404