import allure
from api.common_api import Api
from test_data.coins.data import coin_id
from test_data.headers import headers_with_token


@allure.step("Verify that the coin is returned by the id")
def test_get_coin_by_id():
    coin_id_endpoint = "coin/{}".format(coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
