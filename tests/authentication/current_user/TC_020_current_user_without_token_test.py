import allure
from api.user_api import UserApi
from api.common_api import Api
from test_data.headers import headers
from test_data.user_data.data import valid_user_data


@allure.step("Verify no users returned without token")
def test_current_user_with_no_token_valid_id():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(valid_user_data)
    id = result["response"]["id"]
    current_user_api = Api("api/users/currentuser/{}".format(id))
    result = current_user_api.get_request(headers=headers)
    status_code = result['status_code']
    assert status_code == 401


