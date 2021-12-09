import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("verify coin get all successful test")
def test_coin_get_all():
    api = Api("common/coin/get-all")
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
