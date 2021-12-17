import allure
from api.common_api import Api
from test_data.bank_data.data import new_bank
from test_data.headers import admin_headers_with_token


@allure.step("verify bank is deleted")
def test_delete_bank_by_id():
    """First create a bank and then get the id of it and then delete it"""
    bank_create_api = Api("bank/create")
    create_result = bank_create_api.post_request(new_bank, headers=admin_headers_with_token)
    bank_id_to_delete = create_result['response']['data']['_id']
    delete_api_endpoint = "bank/{}".format(bank_id_to_delete)
    delete_api = Api(delete_api_endpoint)
    delete_result = delete_api.delete_request(headers=admin_headers_with_token)
    status_code = delete_result['status_code']
    assert status_code == 200
