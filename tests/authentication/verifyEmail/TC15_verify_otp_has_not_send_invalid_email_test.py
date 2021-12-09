import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import only_invalid_email


@allure.step("Verify OTP has not send invalid email test")
def test_otp_not_send_to_invalid_email_ac():
    verify_api = VerifyApi("api/auth/verify-email")
    response = verify_api.send_otp(only_invalid_email)
    status_code = response['status_code']
    message = response['response']['message']
    assert status_code == 400
    assert message == "Could not find your Account"

