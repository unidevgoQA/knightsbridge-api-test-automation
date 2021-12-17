import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.crypto_wallet.data import update_crypto_wallet_data


@allure.step("Verify update wallet fail by no token")
def test_update_wallet():
    crypto_api = Api("cryptoWallet/get-all")
    result = crypto_api.get_request(headers=admin_headers_with_token)
    wallet_id = result['response']['data'][0]['_id']
    update_api_endpoint = "cryptoWallet/{}".format(wallet_id)
    update_api = Api(update_api_endpoint)
    result = update_api.put_request(payload=update_crypto_wallet_data)
    status_code = result['status_code']
    assert status_code == 401
