import allure
from api.common_api import Api


@allure.step("Verify update wallet successfully")
def test_get_all_crypto_wallets_fail():
    order_api = Api("cryptoWallet/get-all")
    result = order_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
