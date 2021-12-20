import allure
from api.common_api import Api
from test_data.surveys.data import new_survey
from test_data.headers import admin_headers_with_token


@allure.step("Verify survey not add with get request")
def test_add_surveys():
    api_endpoint = "survey/add"
    survey_api = Api(api_endpoint)
    result = survey_api.get_request(payload=new_survey, headers=admin_headers_with_token)
    message = result["response"]["message"]
    assert message == "Internal server error"
