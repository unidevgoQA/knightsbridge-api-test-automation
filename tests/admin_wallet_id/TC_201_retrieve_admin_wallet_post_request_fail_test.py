import allure
from api.common_api import Api
from test_data.admin_wallet.data import random_wallet_id


@allure.step("Verify that admin can not retrieve admin wallet with post reqeust")
def test_retrieve_admin_wallet_id():
    admin_wallet_api = Api("adminWallet/{}".format(random_wallet_id))
    admin_wallet_api = admin_wallet_api.get_request()
    status_code = admin_wallet_api['status_code']
    assert status_code == 401
