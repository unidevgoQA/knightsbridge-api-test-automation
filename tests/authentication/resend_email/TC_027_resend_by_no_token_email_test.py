import allure
from api.common_api import Api
from test_data.user_data.data import only_invalid_email
from api.config import constData


@allure.step("Resend email by no token verify response code")
def test_resend_no_token_with_valid_id():
    resend_email_api = Api(constData['RESEND_EMAIL'].format(only_invalid_email['email']))
    result = resend_email_api.get_request()
    status_code = result['status_code']
    message = result['response']['error']
    assert message == 'User does not exist'
    assert status_code == 200
