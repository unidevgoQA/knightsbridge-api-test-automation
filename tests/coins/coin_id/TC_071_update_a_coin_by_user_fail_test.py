import allure
from api.common_api import Api
from test_data.coins.data import coin_id_to_update, update_coin_data
from test_data.headers import headers_with_token


@allure.step("Verify that user can't update a coin by id")
def test_coin_updates_by_user():
    coin_id_endpoint = "coin/{}".format(coin_id_to_update)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.put_request(update_coin_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
