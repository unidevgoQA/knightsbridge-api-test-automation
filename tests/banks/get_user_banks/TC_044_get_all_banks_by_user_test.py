import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.bank_data.data import random_bank_user_id


@allure.step("Verify that we can get all banks by user")
def test_banks_returns_by_user():
    api_endpoint = "bank/get-all-user-banks/{}".format(random_bank_user_id)
    api = Api(api_endpoint)
    result = api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
