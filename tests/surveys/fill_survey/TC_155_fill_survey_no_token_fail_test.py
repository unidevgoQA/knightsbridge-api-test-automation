import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.surveys.data import random_survey_id, filL_survey


@allure.step("Verify that user can't fill survey without token")
def test_fill_survey_no_token():
    api_endpoint = "survey/submit/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.post_request(payload=filL_survey)
    status_code = result['status_code']
    assert status_code == 401
