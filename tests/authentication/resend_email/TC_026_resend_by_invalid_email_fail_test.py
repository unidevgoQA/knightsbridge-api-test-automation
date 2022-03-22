import allure
from api.user_api import UserApi
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.user_data.data import valid_user_data, only_invalid_email
from api.config import constData


@allure.step("Resend id by invalid id verify response code")
def test_resend_with_invalid_id():
    user_api = UserApi("api/users/signin")
    sign_in_result = user_api.sign_in_user(valid_user_data)
    user_id = sign_in_result["response"]["id"]
    resend_id_api = Api(constData['RESEND_ID'].format(only_invalid_email['email']+"1sdfsd"))
    result = resend_id_api.get_request(headers=headers_with_token)
    message = result["response"]["message"]
    assert message == "Internal server error"
