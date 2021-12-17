import allure
from api.common_api import Api
from test_data.crypto_deposit.data import new_crypto_deposit
from test_data.headers import admin_headers_with_token


@allure.step("Verify crypto deposit no token fail test")
def test_crypto_deposit():
    api_endpoint = "cryptoDeposit"
    crypto_api = Api(api_endpoint)
    result = crypto_api.post_request(payload=new_crypto_deposit, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201

