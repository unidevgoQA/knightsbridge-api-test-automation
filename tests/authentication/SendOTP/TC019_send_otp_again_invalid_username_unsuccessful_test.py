import allure
from api.verify_api import VerifyApi
from test_data.user_data.data import current_user_name_invalid_data


@allure.step("Send OTP again in invalid username")
def test_send_otp_empty_username():
    verify_api = VerifyApi("api/auth/send-otp")
    response = verify_api.send_otp(current_user_name_invalid_data)
    assert response['status_code'] == 400
