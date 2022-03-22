import allure
from api.common_api import Api
from test_data.expert_trader.data import user_id
from test_data.headers import headers_with_token

@allure.step("Verify that the user status shows properly")

def test_user_status_get_all_valid():
    get_user_status_api = "/copyExperts/userStatus/{}".format(user_id)
    get_user_status_api = Api(get_user_status_api)
    result = get_user_status_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

