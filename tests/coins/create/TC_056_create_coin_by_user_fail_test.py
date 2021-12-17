import allure
from api.common_api import Api
from test_data.coins.data import new_coin
from test_data.headers import headers_with_token


@allure.step("Verify that user can't create coin by user")
def test_create_coin():
    coin_create_api = Api("coin/create")
    result = coin_create_api.post_request(new_coin, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
