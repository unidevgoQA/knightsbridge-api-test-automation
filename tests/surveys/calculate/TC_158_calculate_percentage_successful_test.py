import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.surveys.data import random_survey_id


@allure.step("Verify that the percentage of successful responses is calculated correctly")
def test_calculate_survey():
    api_endpoint = "survey/calculate/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.post_request(
                                    headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
