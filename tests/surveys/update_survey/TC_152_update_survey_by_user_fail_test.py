import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.surveys.data import random_survey_id, update_survey


@allure.step("Verify that user can't update survey by non-admin user")
def test_update_survey_by_user():
    api_endpoint = "survey/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.put_request(payload=update_survey,
                                    headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
