import allure
from api.common_api import Api
from test_data.coins.data import coins_no_type
from test_data.headers import headers_with_token


@allure.step("Verify no coins get by user no coinType fail test")
def test_coins_get_all_no_coin_type_valid():
    coin_api = Api("coin/get-all")
    result = coin_api.get_request(payload=coins_no_type, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
