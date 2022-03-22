import allure
from api.common_api import Api
from test_data.coins.data import invalid_coin_id


@allure.step("Verify that no coin returns without token")
def test_get_coin_by_no_token_fail():
    coin_id_endpoint = "coin/{}".format(invalid_coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
