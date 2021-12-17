import allure
from api.common_api import Api
from test_data.current_user_id import current_user_id
from test_data.headers import headers_with_token


@allure.step("Verify that we can get all banks by user")
def test_banks_returns_by_user():
    api_endpoint = "bank/get-all-user-banks/{}".format(current_user_id)
    api = Api(api_endpoint)
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
