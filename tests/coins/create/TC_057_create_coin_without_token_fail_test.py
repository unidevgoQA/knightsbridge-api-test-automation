import allure
from api.common_api import Api
from test_data.coins.data import new_coin


@allure.step("Verify that user can't create coin without token")
def test_create_coin_fail_without_token():
    coin_create_api = Api("coin/create")
    result = coin_create_api.post_request(new_coin)
    status_code = result['status_code']
    assert status_code == 401
