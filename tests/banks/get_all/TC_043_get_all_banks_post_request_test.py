import allure
from api.common_api import Api


@allure.step("verify that no banks are returned")
def test_no_banks_returns_with_post():
    api = Api("bank/get-all")
    result = api.post_request()
    status_code = result['status_code']
    assert status_code == 404
