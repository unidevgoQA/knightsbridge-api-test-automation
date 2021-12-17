import allure
from api.common_api import Api
from test_data.portfolio_wallet.data import user_id_invalid
from test_data.headers import headers_with_token


@allure.step("Verify retrieve fiat wallet portfolio by no token")
def test_fiat_wallet_portfolio():
    api_endpoint = "portfolio/fiatWallet/{}".format(user_id_invalid)
    fiat_api = Api(api_endpoint)
    result = fiat_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
