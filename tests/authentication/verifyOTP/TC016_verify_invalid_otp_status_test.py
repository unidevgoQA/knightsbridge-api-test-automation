import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import only_valid_email


@allure.step("Verify invalid OTP status test")
def test_invalid_otp_status():
    verify_api = VerifyApi("api/auth/verify-email")
    response = verify_api.send_otp(only_valid_email)
    token = response["response"]["data"]
    verify_otp = VerifyApi("api/auth/verify-otp")
    response = verify_otp.send({"email": "ss.unidev@gmail.com", "otp": "123"},
                               headers={'Authorization': "Bearer " + token, 'Content-Type': 'application/json'})
    assert response['status_code'] == 400