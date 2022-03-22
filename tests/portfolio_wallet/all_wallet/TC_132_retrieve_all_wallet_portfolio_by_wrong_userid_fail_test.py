import allure
from api.common_api import Api
from test_data.portfolio_wallet.data import user_id_invalid
from test_data.headers import headers_with_token


@allure.step("Verify retrieve all wallet portfolio by no token")
def test_all_wallet_portfolio():
    api_endpoint = "portfolio/allWallet/{}".format(user_id_invalid)
    fiat_api = Api(api_endpoint)
    result = fiat_api.get_request(headers=headers_with_token)
    wallet = result['response']['data']['cryptoWallet']
    assert wallet == []
