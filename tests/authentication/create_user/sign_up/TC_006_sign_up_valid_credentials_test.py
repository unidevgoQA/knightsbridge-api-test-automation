import allure
from api.user_api import UserApi
from test_data.user_data.data import user_signup_data


@allure.step('Sign up with valid user data')
def test_success_user_sign_up():
    user_api = UserApi("api/users/signup")
    result = user_api.sign_up_user(user_signup_data)
    response = result["status_code"]
    is_success = True if response == 201 else False
    assert is_success
