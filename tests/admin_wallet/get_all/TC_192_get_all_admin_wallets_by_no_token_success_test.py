import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify that  admin wallets are returned without user token")
def test_get_all_admin_wallets():
    admin_wallet_api = Api("adminWallet/get-all")
    admin_wallet_api = admin_wallet_api.get_request(headers=headers_with_token)
    status_code = admin_wallet_api['status_code']
    assert status_code == 200
    