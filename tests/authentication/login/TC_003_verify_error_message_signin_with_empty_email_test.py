import allure
from test_data.user_data.data import empty_email_data
from api.user_api import UserApi


@allure.step('Verify error message signin with empty username')
def test_invalid_sign_in_empty_username():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(empty_email_data)
    response = result["status_code"]
    assert response == 401


