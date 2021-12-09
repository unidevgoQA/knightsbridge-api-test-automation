import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify that the crypto scan is successful")
def test_crypto_scan_success():
    api = Api("common/crypto/scan")
    result = api.post_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
