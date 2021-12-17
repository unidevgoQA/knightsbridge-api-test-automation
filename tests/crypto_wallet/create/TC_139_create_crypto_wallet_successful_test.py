import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.crypto_wallet.data import new_crypto_wallet


@allure.step("Verify crypto_wallet creation successful")
def test_crypto_wallet_create():
    order_api = Api("cryptoWallet/create")
    result = order_api.post_request(new_crypto_wallet, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
