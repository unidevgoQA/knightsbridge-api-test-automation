import allure
from api.user_api import UserApi
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.user_data.data import valid_user_data
from api.config import constData


@allure.step("Resend id by id test success")
def test_resend_with_valid_id():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(valid_user_data)
    user_id = result["response"]["id"]
    resend_id_api = Api(constData['RESEND_ID'].format(user_id))
    result = resend_id_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
