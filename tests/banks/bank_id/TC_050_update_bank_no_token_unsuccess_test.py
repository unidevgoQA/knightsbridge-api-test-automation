import allure
from api.common_api import Api
from test_data.bank_data.data import bank_id, updated_bank_data


@allure.step("Verify that user can't update bank without token")
def test_update_bank_no_token():
    api_endpoint = "bank/{}".format(bank_id)
    api = Api(api_endpoint)
    result = api.put_request(updated_bank_data)
    status_code = result['status_code']
    assert status_code == 401
