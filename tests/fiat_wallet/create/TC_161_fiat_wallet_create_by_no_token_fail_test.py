import allure
from api.common_api import Api
from test_data.fiat_wallet.data import new_fiat_wallet_data


@allure.step("Verify create fiat wallet by user token fail no token test")
def test_create_fiat_wallet_no_token():
    fiat_api = Api("fiatWallet/create")
    result = fiat_api.post_request(new_fiat_wallet_data)

    status_code = result['status_code']
    assert status_code == 401
