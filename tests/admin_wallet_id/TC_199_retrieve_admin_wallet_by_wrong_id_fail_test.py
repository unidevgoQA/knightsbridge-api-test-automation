import allure
from api.common_api import Api
from test_data.admin_wallet.data import wallet_id_invalid
from test_data.headers import headers_with_token


@allure.step("Verify that admin can't retrieve admin wallet by wrong id")
def test_retrieve_admin_wallet_id():
    admin_wallet_api = Api("adminWallet/{}".format(wallet_id_invalid))
    result = admin_wallet_api.get_request(headers=headers_with_token)
    message = result['response']['message']
    assert message == "Internal server error"
