import allure
from api.common_api import Api
from test_data.crypto_deposit.data import new_crypto_deposit


@allure.step("Verify crypto deposit get successful test")
def test_get_crypto_deposit():
    api_endpoint = "cryptoDeposit"
    crypto_api = Api(api_endpoint)
    result = crypto_api.post_request(payload=new_crypto_deposit)
    status_code = result['status_code']
    assert status_code == 401

