import allure
from api.common_api import Api
from test_data.bank_data.data import bank_id


@allure.step("Verify that the user can not get bank by id with no token")
def test_no_bank_returns_by_bank_id():
    api_endpoint = "bank/{}".format(bank_id)
    api = Api(api_endpoint)
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401
