import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify that the user can get all surveys")
def test_get_surveys():
    api_endpoint = "survey/get-all"
    survey_api = Api(api_endpoint)
    result = survey_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

