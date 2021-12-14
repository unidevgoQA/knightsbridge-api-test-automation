import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.crypto_wallet.data import crypto_wallet_id


@allure.step("Verify retrieve crypto wallet successfully test")
def test_retrieve_wallet():
    api_endpoint = "cryptoWallet/{}".format(crypto_wallet_id)
    crypto_api = Api(api_endpoint)
    result = crypto_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
