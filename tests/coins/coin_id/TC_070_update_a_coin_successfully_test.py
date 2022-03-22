import allure
from api.common_api import Api
from test_data.coins.data import random_coin_id, update_coin_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the coin is updated successfully")
def test_coin_updates_successfully():
    coin_id_endpoint = "coin/{}".format(random_coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.put_request(update_coin_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
