import allure
from api.common_api import Api
from test_data.surveys.data import new_survey


@allure.step("Verify that user can't add survey by no token")
def test_add_survey_no_token():
    api_endpoint = "survey/add"
    survey_api = Api(api_endpoint)
    result = survey_api.post_request(payload=new_survey)
    status_code = result['status_code']
    assert status_code == 401

