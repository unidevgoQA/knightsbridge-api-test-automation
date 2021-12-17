import allure
from api.common_api import Api
from test_data.fiat.data import admin_deposit
from test_data.headers import admin_headers_with_token


@allure.step("Verify admin deposit successful test")
def test_admin_deposit():
    api_endpoint = "fiat/admin-deposit"
    fiat_api = Api(api_endpoint)
    result = fiat_api.post_request(admin_deposit, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

