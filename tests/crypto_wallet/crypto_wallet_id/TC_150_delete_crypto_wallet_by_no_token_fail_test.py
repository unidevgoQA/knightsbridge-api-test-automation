import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.crypto_wallet.data import new_crypto_wallet


@allure.step("Verify update wallet fail no token")
def test_delete_wallet():
    create_api = Api("cryptoWallet/create")
    result = create_api.post_request(new_crypto_wallet, headers=admin_headers_with_token)
    wallet_id = result['response']['data']['_id']
    delete_api_endpoint = "cryptoWallet/{}".format(wallet_id)
    delete_api = Api(delete_api_endpoint)
    result = delete_api.delete_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
