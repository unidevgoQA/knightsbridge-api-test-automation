import allure
from api.common_api import Api


@allure.step("Verify that the user can not get the settings without token")
def test_common_settings_get_no_token_request():
    api = Api("common/settings")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 200
