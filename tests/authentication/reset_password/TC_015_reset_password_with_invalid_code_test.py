import allure
from api.common_api import Api
from test_data.reset_password.data import \
    reset_user_data_only_email,\
    reset_email_with_invalid_code


@allure.step("Reset password with invalid token Unsuccessful")
def test_reset_password_unsuccessful_invalid_code():
    forgot_api = Api("api/users/forgot-password")
    reset_api = Api("api/users/reset-password")
    forgot_api.post_request(reset_user_data_only_email)
    reset_response = reset_api.send(reset_email_with_invalid_code)
    reset_response['status_code'] = 400

