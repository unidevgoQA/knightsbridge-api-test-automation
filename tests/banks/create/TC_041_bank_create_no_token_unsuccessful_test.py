import allure
from api.common_api import Api
from test_data.bank_data.data import new_bank


@allure.step("verify bank create no token unsuccessful test")
def test_no_token_bank_create():
    api = Api("bank/create")
    result = api.post_request(new_bank)
    status_code = result['status_code']
    assert status_code == 401
