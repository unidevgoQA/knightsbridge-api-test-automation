import allure
from api.common_api import Api
from test_data.bank_data.data import invalid_bank_id
from test_data.headers import headers_with_token


@allure.step("Delete bank by user fail test")
def test_delete_bank_by_user():
    delete_api_endpoint = "bank/{}".format(invalid_bank_id)
    delete_api = Api(delete_api_endpoint)
    delete_result = delete_api.delete_request(headers=headers_with_token)
    status_code = delete_result['status_code']
    assert status_code == 403
