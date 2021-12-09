import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import only_valid_email


@allure.step("Verify OTP has been successfully sent")
def test_otp_sends_for_valid_email():
    verify_api = VerifyApi("api/auth/verify-email")
    response = verify_api.send_otp(only_valid_email)
    status_code = response['status_code']
    message = response['response']['message']
    assert status_code == 201
    assert message == "OTP has been sent to you via email."

