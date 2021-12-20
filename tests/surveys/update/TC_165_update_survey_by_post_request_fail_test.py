import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.surveys.data import random_survey_id, update_survey_data


@allure.step("Verify that update survey by post request fail")
def test_update_path_survey():
    api_endpoint = "survey/update/{}".format(random_survey_id)
    survey_api = Api(api_endpoint)
    result = survey_api.post_request(payload=update_survey_data,
                                    headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
