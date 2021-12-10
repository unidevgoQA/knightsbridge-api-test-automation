import allure
from api.common_api import Api
from test_data.coins.data import coin_id_to_update, update_coin_data
from test_data.headers import headers_with_token


@allure.step("Verify that update a coin with no token fails")
def test_coin_updates_no_token():
    coin_id_endpoint = "coin/{}".format(coin_id_to_update)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.put_request(update_coin_data)
    status_code = result['status_code']
    assert status_code == 401
