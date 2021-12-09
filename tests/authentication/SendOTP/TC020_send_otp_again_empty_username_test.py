import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import current_user_name_empty_data


@allure.step("Send OTP again empty username test")
def test_send_otp_again_empty_email():
    verify_api = VerifyApi("api/auth/send-otp")
    response = verify_api.send_otp(current_user_name_empty_data)
    assert response['status_code'] == 400
