import allure
from api.common_api import Api
from test_data.fiat_wallet.data import fiat_wallet_user_id, fiat_wallet_update_data


@allure.step("Verify retrieve fiat wallet by user id no user token fail test")
def test_update_fiat_wallet_user_id():
    fiat_api = Api("fiatWallet/update/{}".format(fiat_wallet_user_id))
    fiat_api = fiat_api.put_request(payload=fiat_wallet_update_data)
    status_code = fiat_api['status_code']
    assert status_code == 401
