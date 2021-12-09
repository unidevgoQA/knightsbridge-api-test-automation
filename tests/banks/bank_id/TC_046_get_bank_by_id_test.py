import allure
from api.common_api import Api
from test_data.bank_data.data import bank_id
from test_data.headers import headers_with_token


@allure.step("Verify that the user can get bank by id")
def test_bank_returns_by_bank_id():
    api_endpoint = "bank/{}".format(bank_id)
    api = Api(api_endpoint)
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
