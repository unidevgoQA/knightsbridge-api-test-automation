import allure
from api.common_api import Api
from test_data.fiat_wallet.data import random_fiat_wallet_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify retrieve fiat wallet by id success test")
def test_retrieve_fiat_wallet():
    endpoint = "fiatWallet/{}".format(random_fiat_wallet_id)
    fiat_api = Api(endpoint)
    result = fiat_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
