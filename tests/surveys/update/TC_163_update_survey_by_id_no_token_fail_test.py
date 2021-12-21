import allure
from api.common_api import Api
from test_data.surveys.data import random_survey_id, update_survey_data


@allure.step("Verify that the user can't update a survey by id without token")
def test_update_path_survey_no_token():
    api_endpoint = "survey/update/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.put_request(payload=update_survey_data)
    status_code = result['status_code']
    assert status_code == 401
