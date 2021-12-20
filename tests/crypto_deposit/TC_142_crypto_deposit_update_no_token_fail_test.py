import allure
from api.common_api import Api
from test_data.crypto_deposit.data import status, deposit_id


@allure.step("Verify crypto deposit update no token fail test")
def test_update_crypto_deposit():
    api_endpoint = "cryptoDeposit/{}/{}".format(deposit_id, status)
    deposit_api = Api(api_endpoint)
    deposit_result = deposit_api.put_request()
    message = deposit_result['response']['message']
    assert message == 'Internal server error'
