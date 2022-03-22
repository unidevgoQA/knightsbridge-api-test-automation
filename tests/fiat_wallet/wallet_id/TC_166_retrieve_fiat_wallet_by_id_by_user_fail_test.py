import allure
from api.common_api import Api
from test_data.fiat_wallet.data import fiat_wallet_id
from test_data.headers import headers_with_token


@allure.step("Verify retrieve fiat wallet by id by user fail test")
def test_retrieve_fiat_wallet():
    endpoint = "fiatWallet/{}".format(fiat_wallet_id)
    fiat_api = Api(endpoint)
    result = fiat_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
