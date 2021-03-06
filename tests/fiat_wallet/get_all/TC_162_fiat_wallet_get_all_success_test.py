import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can get all fiat wallets")
def test_get_all_fiat_wallets():
    fiat_api = Api("fiatWallet/get-all")
    result = fiat_api.get_request(headers=admin_headers_with_token)

    status_code = result['status_code']
    assert status_code == 200
