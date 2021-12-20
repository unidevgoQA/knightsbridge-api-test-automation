import allure
from api.common_api import Api
from test_data.portfolio_wallet.data import random_user_id
from test_data.headers import headers_with_token


@allure.step("Verify retrieve all wallet portfolio by userid")
def test_all_wallet_portfolio():
    api_endpoint = "portfolio/allWallet/{}".format(random_user_id)
    fiat_api = Api(api_endpoint)
    result = fiat_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
