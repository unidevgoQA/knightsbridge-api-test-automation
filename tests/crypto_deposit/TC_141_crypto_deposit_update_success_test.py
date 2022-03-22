import allure
from api.common_api import Api
from test_data.crypto_deposit.data import new_crypto_deposit, status
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can update crypto deposit")
def test_update_crypto_deposit():
    api_endpoint = "cryptoDeposit"
    crypto_api = Api(api_endpoint)
    result = crypto_api.post_request(payload=new_crypto_deposit, headers=admin_headers_with_token)
    deposit_id = result['response']['data']['_id']
    api_endpoint = "cryptoDeposit/{}/{}".format(deposit_id, status)
    deposit_api = Api(api_endpoint)
    deposit_result = deposit_api.put_request(headers=admin_headers_with_token)
    status_code = deposit_result['status_code']
    assert status_code == 200
