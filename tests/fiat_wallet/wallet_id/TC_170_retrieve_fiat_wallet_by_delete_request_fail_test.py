import allure
from api.common_api import Api
from test_data.fiat_wallet.data import fiat_wallet_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can update fiat wallet by valid data")
def test_update_fiat_wallet():
    endpoint = "fiatWallet/{}".format(fiat_wallet_id)
    fiat_api = Api(endpoint)
    result = fiat_api.put_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200