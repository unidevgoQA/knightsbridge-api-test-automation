import allure
from api.common_api import Api
from test_data.coins.data import new_coin
from test_data.headers import admin_headers_with_token


@allure.step("Verify create coin success")
def test_create_coin():
    coin_create_api = Api("coin/create")
    result = coin_create_api.post_request(new_coin, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
