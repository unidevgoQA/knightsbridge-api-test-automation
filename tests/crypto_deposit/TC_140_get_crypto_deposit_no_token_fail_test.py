import allure
from api.common_api import Api


@allure.step("Verify crypto deposit get successful test")
def test_get_crypto_deposit():
    api_endpoint = "cryptoDeposit?pageSize={}&pageNumber={}".format(1, 1)
    crypto_api = Api(api_endpoint)
    result = crypto_api.get_request()
    status_code = result['status_code']
    assert status_code == 401

