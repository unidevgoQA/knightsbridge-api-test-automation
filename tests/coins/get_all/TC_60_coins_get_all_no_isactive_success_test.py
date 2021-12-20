import allure
from api.common_api import Api
from test_data.coins.data import coins_get_no_is_active
from test_data.headers import headers_with_token


@allure.step("Verify coins get all no is_active success test")
def test_coins_get_all_no_is_active_valid():
    coin_api = Api("coin/get-all")
    result = coin_api.get_request(payload=coins_get_no_is_active, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
