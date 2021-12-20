import allure
from api.common_api import Api
from test_data.admin_wallet.data import random_wallet_id
from test_data.headers import headers_with_token


@allure.step("Verify that admin wallet is retrieved by success")
def test_retrieve_admin_wallet_id():
    admin_wallet_api = Api("adminWallet/{}".format(random_wallet_id))
    admin_wallet_api = admin_wallet_api.get_request( headers=headers_with_token)
    status_code = admin_wallet_api['status_code']
    assert status_code == 200
