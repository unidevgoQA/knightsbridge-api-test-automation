import allure
from api.common_api import Api
from test_data.fiat.data import fiat_withdraw, user_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify get withdraw successful")
def test_withdraw_money():
    api_endpoint = "fiat/withdraw?userId={}&pageSize=1&pageNumber=1&search=".format(user_id)
    fiat_api = Api(api_endpoint)
    result = fiat_api.post_request(fiat_withdraw, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 401


