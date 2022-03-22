import allure
from api.common_api import Api


@allure.step("Verify delete fiat wallet by get request fail test")
def test_delete_fiat_wallet():
    delete_api = Api("fiatWallet/565467867987987978")
    delete_result = delete_api.post_request()
    status_code = delete_result['status_code']
    assert status_code == 404
