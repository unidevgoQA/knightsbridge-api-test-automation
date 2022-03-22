import allure
from api.common_api import Api
from test_data.common_data.data import new_coin


@allure.step("verify coin create no token unsuccessful test")
def test_coin_no_token_create():
    api = Api("common/coin/create")
    result = api.post_request(new_coin)
    status_code = result['status_code']
    assert status_code == 401
