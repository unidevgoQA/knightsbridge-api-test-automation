import allure
from api.common_api import Api
from test_data.crypto_wallet.data import exist_wallet


@allure.step("Verify crypto_wallet creation fail no token")
def test_crypto_wallet_create_no_token():
    order_api = Api("cryptoWallet/create")
    result = order_api.post_request(exist_wallet)
    status_code = result['status_code']
    assert status_code == 401
