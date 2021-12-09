import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.user_data.data import only_invalid_email
from api.config import constData


@allure.step("Resend email by invalid email test")
def test_resend_with_valid_id():
    resend_email_api = Api(constData['RESEND_EMAIL'].format(only_invalid_email['email']))
    result = resend_email_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    message = result['response']['error']
    assert status_code == 200
    assert message == 'User does not exist'