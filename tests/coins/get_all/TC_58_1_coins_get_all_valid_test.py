import allure
from api.common_api import Api
from test_data.coins.data import coins_get_all_params
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the user can get all coins")
def test_coins_get_all_valid():
    coin_type_endpoint = "coin/get-all?isActive={}&coinType={}". \
        format(coins_get_all_params['isActive'],
               coins_get_all_params['coinType'])
    coin_api = Api(coin_type_endpoint)
    result = coin_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
