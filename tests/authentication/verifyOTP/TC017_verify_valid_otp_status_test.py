import allure
from time import sleep
from api.verify_api import VerifyApi
from test_data.user_data.data import only_valid_email
from utils.email_reader import get_otp_from_email
from test_data.common_data import email


@allure.step("Verify valid OTP status test successful")
def test_valid_otp_status_verification():
    verify_api = VerifyApi("api/auth/verify-email")
    response = verify_api.send_otp(only_valid_email)
    token = response["response"]["data"]
    sleep(30)
    verify_otp = VerifyApi("api/auth/verify-otp")
    response = verify_otp.send({"email": "ss.unidev@gmail.com", "otp": get_otp_from_email(email)},
                               headers={'Authorization': "Bearer " + token, 'Content-Type': 'application/json'})
    message = response["response"]["message"]
    assert response['status_code'] == 201
    assert message == "OTP has been verified."

