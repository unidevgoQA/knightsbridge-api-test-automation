import allure
from api.common_api import Api
from test_data.surveys.data import random_survey_id


@allure.step("Verify that user can't calculate percentage without token")
def test_calculate_survey():
    api_endpoint = "survey/calculate/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.post_request()
    status_code = result['status_code']
    assert status_code == 401
