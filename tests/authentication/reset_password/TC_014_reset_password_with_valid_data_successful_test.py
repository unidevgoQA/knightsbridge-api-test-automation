import time
import allure
from api.common_api import Api
from test_data.reset_password.data import \
    reset_user_data_only_email, \
    reset_email_credentials, \
    reset_email_with_code
from utils.email_reader import get_otp_from_email


@allure.step("Reset password with valid data successful")
def test_reset_password_successful():
    forgot_api = Api("api/users/forgot-password")
    reset_api = Api("api/users/reset-password")
    forgot_api.post_request(reset_user_data_only_email)
    time.sleep(30)
    payload = reset_email_with_code['code'] = get_otp_from_email(reset_email_credentials)
    reset_response = reset_api.send(payload)
    reset_response['status_code'] = 201
