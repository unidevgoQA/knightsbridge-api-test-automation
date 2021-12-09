import allure
from api.common_api import Api


@allure.step("verify that all banks are returned")
def test_all_banks_returns():
    api = Api("bank/get-all")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 200
