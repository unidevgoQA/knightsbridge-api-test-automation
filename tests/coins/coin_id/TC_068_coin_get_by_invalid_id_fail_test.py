import allure
from api.common_api import Api
from test_data.coins.data import invalid_coin_id
from test_data.headers import headers_with_token


@allure.step("Verify that no coin is returned by the invalid id")
def test_get_coin_by_invalid_id():
    coin_id_endpoint = "coin/{}".format(invalid_coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.get_request(headers=headers_with_token)
    message = result['response']['message']
    assert message == 'Internal server error'
