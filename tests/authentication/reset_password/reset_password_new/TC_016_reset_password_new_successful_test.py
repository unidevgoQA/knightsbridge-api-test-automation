import allure
from time import sleep
from api.common_api import Api
from test_data.reset_password.data import reset_email_credentials
from test_data.reset_password.data import \
    reset_user_data_only_email,\
    reset_email_with_code,\
    new_password
from utils.email_reader import get_otp_from_email


@allure.step("Reset password new with valid email and code and valid password")
def test_reset_password_new_successful():
    forgot_api = Api("api/users/forgot-password")
    reset_api = Api("api/users/reset-password")
    reset_new_password_api = Api("api/users/reset-password/new")
    forgot_api.post_request(reset_user_data_only_email)
    sleep(30)
    reset_email_with_code['code'] = get_otp_from_email(reset_email_credentials)
    reset_response = reset_api.send(reset_email_with_code)
    token = reset_response['response']['token']
    payload = {"token": token, "password": new_password}
    reset_password_response = reset_new_password_api.send(payload)
    reset_password_response['status_code'] = 201
