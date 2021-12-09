import allure
from api.common_api import Api
from test_data.common_data.data import new_coin
from test_data.headers import headers_with_token


@allure.step("Verify that user can create coin successfully")
def test_coin_create():
    api = Api("common/coin/create")
    result = api.post_request(new_coin, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
