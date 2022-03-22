import allure
from api.common_api import Api
from test_data.bank_data.data import bank_id, updated_bank_data
from test_data.headers import headers_with_token


@allure.step("Verify that user can't update bank by user token")
def test_update_bank_details_by_user():
    api_endpoint = "bank/{}".format(bank_id)
    api = Api(api_endpoint)
    result = api.put_request(updated_bank_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
