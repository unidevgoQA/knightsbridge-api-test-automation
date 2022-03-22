import allure
from api.common_api import Api
from test_data.current_user_id import current_user_id


@allure.step("Verify can not get transaction information without user token")
def test_transactions_for_no_token():
    api_endpoint = "transaction/{}".format(current_user_id)
    status_api = Api(api_endpoint)
    result = status_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
