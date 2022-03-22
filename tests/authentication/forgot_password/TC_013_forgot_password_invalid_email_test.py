import allure
from api.user_api import UserApi
from test_data.user_data.data import only_invalid_email


@allure.step('Forgot password with invalid email')
def test_forgot_password_invalid_email():
    user_api = UserApi("api/users/forgot-password")
    result = user_api.post_request(only_invalid_email)
    message = result["response"]["error"]
    assert message == "User does not exist"
