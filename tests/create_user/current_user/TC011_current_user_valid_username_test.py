import allure
from api.user_api import UserApi
from test_data.user_data.data import current_user_name_valid_data


@allure.step("Test current user valid username test")
def test_current_user_with_valid_username():
    user_api = UserApi("api/get-user-by-username")
    result = user_api.sign_up_user(current_user_name_valid_data)
    status_code = result["status_code"]
    assert status_code == 201


