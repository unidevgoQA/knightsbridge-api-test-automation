import allure
from api.common_api import Api
from test_data.coins.data import coin_id


@allure.step("Verify that user can't delete a coin by id without token")
def test_coin_not_delete_no_token():
    coin_id_endpoint = "coin/{}".format(coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.delete_request()
    status_code = result['status_code']
    assert status_code == 401
