import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.fiat_wallet.data import fiat_wallet_user_id


@allure.step("Verify retrieve fiat wallet by user id post request fail test")
def test_retrieve_fiat_wallet():
    fiat_api = Api("fiatWallet/{}".format(fiat_wallet_user_id))
    fiat_api = fiat_api.post_request(headers=admin_headers_with_token)
    status_code = fiat_api['status_code']
    assert status_code == 404
