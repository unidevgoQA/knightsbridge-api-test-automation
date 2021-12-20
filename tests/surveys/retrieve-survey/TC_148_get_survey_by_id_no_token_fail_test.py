import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.surveys.data import random_survey_id


@allure.step("Verify that the user can't get survey by id without token")
def test_get_survey():
    api_endpoint = "survey/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.get_request()
    status_code = result['status_code']
    assert status_code == 401

