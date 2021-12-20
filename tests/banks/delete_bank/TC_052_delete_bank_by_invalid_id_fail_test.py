import allure
from api.common_api import Api
from test_data.bank_data.data import invalid_bank_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can't delete bank by invalid id")
def test_delete_bank_by_invalid_id():
    """ Try to delete a bank with an invalid bank id"""
    delete_api_endpoint = "bank/{}".format(invalid_bank_id)
    delete_api = Api(delete_api_endpoint)
    delete_result = delete_api.delete_request(headers=admin_headers_with_token)
    message = delete_result['response']['message']
    assert message == "Internal server error"
