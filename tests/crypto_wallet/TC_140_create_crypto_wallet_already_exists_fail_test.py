import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.crypto_wallet.data import exist_wallet


@allure.step("Verify crypto_wallet creation fail existing")
def test_crypto_wallet_create():
    order_api = Api("cryptoWallet/create")
    result = order_api.post_request(exist_wallet, headers=admin_headers_with_token)
    status_code = result['status_code']
    message = result['response']['error']
    assert status_code == 201
    assert message == 'Crypto Wallet Already Exists.'
