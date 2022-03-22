import allure
from api.common_api import Api
from test_data.orchestration.data import mail_data_empty_to


@allure.step("Verify user can not send mail without to address")
def test_send_mail_without_to():
    orchestration_api = Api("sendMail")
    result = orchestration_api.post_request(payload=mail_data_empty_to)
    message = result['response']['message']
    assert message == "Internal server error"
