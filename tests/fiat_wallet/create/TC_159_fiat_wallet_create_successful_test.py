import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.fiat_wallet.data import new_fiat_wallet_data


@allure.step("Verify create fiat wallet successful")
def test_create_fiat_wallet():
    fiat_api = Api("fiatWallet/create")
    result = fiat_api.post_request(new_fiat_wallet_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
