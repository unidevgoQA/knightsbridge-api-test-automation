import allure
from api.common_api import Api
from test_data.coins.data import coin_to_search
from test_data.headers import headers_with_token


@allure.step("Verify that user can't get coin market search result by user token")
def test_coin_market_search_by_user():
    coin_api = Api("coin/get-coinMarket?search={}".format(coin_to_search))
    result = coin_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
