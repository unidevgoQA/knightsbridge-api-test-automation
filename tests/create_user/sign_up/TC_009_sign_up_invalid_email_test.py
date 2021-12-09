import allure
from api.user_api import UserApi
from test_data.user_data.data import user_signup_invalid_email


@allure.step("Sign up with invalid email")
def test_sign_up_invalid_email():
    user_api = UserApi("api/users/signup")
    result = user_api.sign_up_user(user_signup_invalid_email)
    status_code = result["status_code"]
    assert status_code == 400
    assert result["response"]["message"][0] == "email must be an email"

