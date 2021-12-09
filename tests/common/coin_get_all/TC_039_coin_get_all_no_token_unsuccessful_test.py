import allure
from api.common_api import Api


@allure.step("verify coin get all no-token unsuccessful test")
def test_coin_get_all_no_token():
    api = Api("common/coin/get-all")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401
