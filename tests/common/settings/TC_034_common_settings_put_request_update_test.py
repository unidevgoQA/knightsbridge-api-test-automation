import allure
from api.common_api import Api
from test_data.common_data.data import new_fee
from test_data.headers import headers_with_token


@allure.step("Verify that the user can not get the settings without token")
def test_common_settings_get_token_request():
    api = Api("common/settings")
    result = api.put_request(new_fee, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
