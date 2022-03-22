import allure
from api.common_api import Api
from test_data.fiat.data import fiat_withdraw
from test_data.headers import headers_with_token


@allure.step("Verify that user can withdraw a fiat wallet")
def test_():
    fiat_api = Api("fiat/withdraw")
    result = fiat_api.post_request(fiat_withdraw, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
