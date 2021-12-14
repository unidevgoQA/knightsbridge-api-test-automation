import allure
from api.common_api import Api


@allure.step("Verify that without token not possible to get all fiat wallets")
def test_no_token_fiat_wallets_fail():
    fiat_api = Api("fiatWallet/get-all")
    result = fiat_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
