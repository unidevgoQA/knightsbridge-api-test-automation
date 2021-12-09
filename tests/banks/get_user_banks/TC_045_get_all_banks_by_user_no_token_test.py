import allure
from api.common_api import Api
from test_data.current_user_id import current_user_id


@allure.step("Verify that user can not get all banks by user id without token")
def test_no_banks_returns_by_user_without_token():
    api_endpoint = "bank/get-all-user-banks/{}".format(current_user_id)
    api = Api(api_endpoint)
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401
