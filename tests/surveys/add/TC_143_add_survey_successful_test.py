import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.surveys.data import new_survey


@allure.step("Verify that user can add survey successfully")
def test_add_surveys():
    api_endpoint = "survey/add"
    survey_api = Api(api_endpoint)
    result = survey_api.post_request(payload=new_survey,
                                     headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
