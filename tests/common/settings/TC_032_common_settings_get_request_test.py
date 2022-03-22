import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify that the user can get the settings")
def test_common_settings_get_request():
    api = Api("common/settings")
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
