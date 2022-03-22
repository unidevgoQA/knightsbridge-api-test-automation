import allure
from api.common_api import Api
from test_data.portfolio_wallet.data import random_user_id


@allure.step("Verify retrieve crypto wallet portfolio by no token")
def test_crypto_wallet_portfolio():
    api_endpoint = "portfolio/cryptoWallet/{}".format(random_user_id)
    fiat_api = Api(api_endpoint)
    result = fiat_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
