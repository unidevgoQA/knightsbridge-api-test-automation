import allure
from api.common_api import Api
from test_data.crypto_wallet.data import update_crypto_wallet_data
from test_data.headers import admin_headers_with_token
from test_data.get_token import admin_id


@allure.step("Update crypto wallet by user id in path success test")
def test_update_crypto_wallet():
    api_endpoint = "cryptoWallet/update/{}".format(admin_id)
    crypto_api = Api(api_endpoint)
    result = crypto_api.put_request(payload=update_crypto_wallet_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
