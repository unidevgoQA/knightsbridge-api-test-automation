import allure
from api.common_api import Api
from test_data.reset_password.data import \
    new_password_with_invalid_token


@allure.step("Reset password new test no token unsuccessful test")
def test_reset_password_new_invalid_token_unsuccessful():
    reset_new_password_api = Api("api/users/reset-password/new")
    reset_password_response = reset_new_password_api.send(new_password_with_invalid_token)
    reset_password_response['status_code'] = 400
