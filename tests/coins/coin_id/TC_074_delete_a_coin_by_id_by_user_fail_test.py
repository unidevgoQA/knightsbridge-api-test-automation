import allure
from api.common_api import Api
from test_data.coins.data import new_coin
from test_data.headers import headers_with_token, admin_headers_with_token


@allure.step("Verify that user can't delete a coin by id")
def test_coin_not_delete_by_user():
    coin_create_api = Api("coin/create")
    result = coin_create_api.post_request(new_coin, headers=admin_headers_with_token)
    coin_id = result['response']['data']['_id']
    coin_id_endpoint = "coin/{}".format(coin_id)
    coin_api = Api(coin_id_endpoint)
    result = coin_api.delete_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
