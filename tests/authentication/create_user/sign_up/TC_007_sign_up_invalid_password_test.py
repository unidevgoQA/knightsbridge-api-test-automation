import allure
from api.user_api import UserApi
from test_data.user_data.data import user_signup_invalid_password


@allure.step("Sign up with invalid password")
def test_success_user_sign_up():
    user_api = UserApi("api/users/signup")
    result = user_api.sign_up_user(user_signup_invalid_password)
    response = result["status_code"]
    assert response == 400
