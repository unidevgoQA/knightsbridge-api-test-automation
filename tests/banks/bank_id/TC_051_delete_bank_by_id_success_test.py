import allure
from api.common_api import Api
from test_data.bank_data.data import bank_id_to_delete
from test_data.headers import admin_headers_with_token, headers_with_token


@allure.step("verify bank is deleted")
def test_update_bank_no_token():
    api_endpoint = "bank/{}".format(bank_id_to_delete)
    api = Api(api_endpoint)
    result = api.delete_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
