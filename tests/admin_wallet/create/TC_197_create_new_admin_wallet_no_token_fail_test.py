import allure
from api.common_api import Api
from test_data.admin_wallet.data import new_admin_wallet


@allure.step("Verify that user can create new admin wallet")
def test_create_admin_wallet():
    admin_wallet_api = Api("adminWallet/create")
    admin_wallet_api = admin_wallet_api.post_request(payload=new_admin_wallet)
    status_code = admin_wallet_api['status_code']
    assert status_code == 401
