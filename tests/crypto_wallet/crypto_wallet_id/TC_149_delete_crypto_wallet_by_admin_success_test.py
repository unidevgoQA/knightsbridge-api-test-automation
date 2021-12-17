import allure
from api.common_api import Api
from test_data.crypto_wallet.data import new_crypto_wallet


@allure.step("Verify update wallet fail by admin")
def test_delete_wallet():
    delete_api_endpoint = "cryptoWallet/61b838976d53f40023955bd3"
    delete_api = Api(delete_api_endpoint)
    result = delete_api.delete_request()
    status_code = result['status_code']
    assert status_code == 401
