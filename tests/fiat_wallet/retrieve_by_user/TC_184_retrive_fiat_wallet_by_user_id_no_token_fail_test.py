import allure
from api.common_api import Api
from test_data.fiat_wallet.data import fiat_wallet_user_id


@allure.step("Verify retrieve fiat wallet by user id no token fail test")
def test_retrieve_fiat_wallet():
    fiat_api = Api("fiatWallet/{}".format(fiat_wallet_user_id))
    fiat_api = fiat_api.get_request()
    status_code = fiat_api['status_code']
    assert status_code == 401
