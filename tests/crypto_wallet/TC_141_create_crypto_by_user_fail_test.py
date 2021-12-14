import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.crypto_wallet.data import exist_wallet


@allure.step("Verify crypto_wallet creation fail by user")
def test_crypto_wallet_create():
    order_api = Api("cryptoWallet/create")
    result = order_api.post_request(exist_wallet, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
