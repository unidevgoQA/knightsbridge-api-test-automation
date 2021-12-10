import allure
from api.common_api import Api
from test_data.orchestration.data import mail_data


@allure.step("Verify user can not send mail successfully with delete request")
def test_send_mail_delete_request():
    orchestration_api = Api("sendMail")
    result = orchestration_api.delete_request()
    status_code = result['status_code']
    assert status_code == 404
