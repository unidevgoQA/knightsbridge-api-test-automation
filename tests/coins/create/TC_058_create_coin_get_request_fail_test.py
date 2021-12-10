import allure
from api.common_api import Api
from test_data.coins.data import new_coin
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can't create coin with get request")
def test_create_coin_fail_get_request():
    coin_create_api = Api("coin/create")
    result = coin_create_api.get_request(new_coin, admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 500
