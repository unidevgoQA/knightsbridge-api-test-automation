import allure
from api.user_api import UserApi
from test_data.user_data.data import user_signup_empty_email


@allure.step("Sign up with empty email")
def test_sign_up_empty_email():
    user_api = UserApi("api/users/signup")
    result = user_api.sign_up_user(user_signup_empty_email)
    status_code = result["status_code"]
    messages = result['response']['message']
    assert status_code == 400
    assert messages[0] == "email must be an email"

