import allure
from api.common_api import Api


@allure.step("Verify get orchestration put request fail test")
def test_orchestration_home_put():
    promotion_api = Api("")
    result = promotion_api.post_request()
    status_code = result['status_code']
    assert status_code == 404
