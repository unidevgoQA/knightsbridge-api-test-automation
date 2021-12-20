import allure
from api.common_api import Api
from test_data.bank_data.data import random_bank_id, updated_bank_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify update bank test")
def test_update_bank_details():
    api_endpoint = "bank/{}".format(random_bank_id)
    api = Api(api_endpoint)
    result = api.put_request(updated_bank_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
