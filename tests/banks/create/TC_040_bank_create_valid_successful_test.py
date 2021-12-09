import allure
from api.common_api import Api
from test_data.bank_data.data import new_bank
from test_data.headers import headers_with_token


@allure.step("verify bank create valid successful")
def test_valid_bank_create():
    api = Api("bank/create")
    result = api.post_request(new_bank, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
