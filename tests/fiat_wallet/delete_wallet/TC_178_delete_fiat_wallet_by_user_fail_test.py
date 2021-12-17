import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token, headers_with_token
from test_data.fiat_wallet.data import new_fiat_wallet_data


@allure.step("Verify delete fiat wallet by user fail test")
def test_delete_fiat_wallet():
    fiat_api = Api("fiatWallet/create")
    result = fiat_api.post_request(new_fiat_wallet_data, headers=admin_headers_with_token)
    wallet_id = result['response']['data']['_id']
    delete_api = Api("fiatWallet/{}".format(wallet_id))
    delete_result = delete_api.delete_request(headers=headers_with_token)
    status_code = delete_result['status_code']
    assert status_code == 403
