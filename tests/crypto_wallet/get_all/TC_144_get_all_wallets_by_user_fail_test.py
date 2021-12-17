import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify get all wallets fail test by user")
def test_get_all_crypto_wallets_fail():
    crypto_api = Api("cryptoWallet/get-all")
    result = crypto_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
