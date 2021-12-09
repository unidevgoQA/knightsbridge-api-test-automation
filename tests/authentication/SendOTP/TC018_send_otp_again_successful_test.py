import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import current_user_name_valid_data


@allure.step("Send OTP again to user test successful")
def test_send_otp_again():
    verify_api = VerifyApi("api/auth/send-otp")
    response = verify_api.send_otp(current_user_name_valid_data)
    assert response['status_code'] == 201
