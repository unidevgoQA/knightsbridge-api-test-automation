import allure
from api.common_api import Api


@allure.step("Verify get orchestration home success test")
def test_orchestration_home():
    promotion_api = Api("")
    result = promotion_api.get_request()
    status_code = result['status_code']
    assert status_code == 200
