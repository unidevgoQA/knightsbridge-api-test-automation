import allure
from api.common_api import Api
from test_data.orchestration.data import mail_data


@allure.step("Verify user can send mail successfully")
def test_send_mail():
    orchestration_api = Api("sendMail")
    result = orchestration_api.post_request(payload=mail_data)
    status_code = result['status_code']
    assert status_code == 201
