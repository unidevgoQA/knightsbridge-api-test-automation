import allure
from api.common_api import Api
from test_data.coins.data import coin_to_search
from test_data.headers import admin_headers_with_token


@allure.step("Verify get coin market search result test returns result")
def test_coin_market_search():
    coin_api = Api("coin/get-coinMarket?search={}".format(coin_to_search))
    result = coin_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
