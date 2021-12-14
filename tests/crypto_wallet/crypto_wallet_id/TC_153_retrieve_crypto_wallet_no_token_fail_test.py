import allure
from api.common_api import Api
from test_data.crypto_wallet.data import crypto_wallet_id


@allure.step("Verify retrieve crypto wallet fail by no token test")
def test_retrieve_wallet_no_token():
    api_endpoint = "cryptoWallet/{}".format(crypto_wallet_id)
    crypto_api = Api(api_endpoint)
    result = crypto_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
