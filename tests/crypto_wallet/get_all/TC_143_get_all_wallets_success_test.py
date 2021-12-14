import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token


@allure.step("Verify get all wallets success test")
def test_get_all_crypto_wallets():
    crypto_api = Api("cryptoWallet/get-all")
    result = crypto_api.get_request(headers=admin_headers_with_token)

    status_code = result['status_code']
    assert status_code == 200
