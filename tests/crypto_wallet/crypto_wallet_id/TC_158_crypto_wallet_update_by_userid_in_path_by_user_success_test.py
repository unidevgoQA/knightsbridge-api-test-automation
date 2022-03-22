import allure
from api.common_api import Api
from test_data.crypto_wallet.data import update_crypto_wallet_data
from test_data.headers import admin_headers_with_token, headers_with_token


@allure.step("Verify a user can update a crypto wallet by user id in path by user")
def test_update_crypto_wallet():
    crypto_api = Api("cryptoWallet/get-all")
    result = crypto_api.get_request(headers=admin_headers_with_token)
    wallet_to_update = result['response']['data'][6]
    api_endpoint = "cryptoWallet/update/{}".format(wallet_to_update['userId'])
    crypto_api = Api(api_endpoint)
    result = crypto_api.put_request(payload=update_crypto_wallet_data,
                                    headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
