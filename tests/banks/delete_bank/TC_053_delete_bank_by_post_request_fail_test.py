import allure
from api.common_api import Api
from test_data.bank_data.data import invalid_bank_id
from test_data.headers import admin_headers_with_token


@allure.step("Delete bank by post request fail test")
def test_delete_bank_by_post_reqeust():
    """ Try to delete a bank with an invalid bank id"""
    delete_api_endpoint = "bank/{}".format(invalid_bank_id)
    delete_api = Api(delete_api_endpoint)
    delete_result = delete_api.post_request(headers=admin_headers_with_token)
    status_code = delete_result['status_code']
    assert status_code == 404
