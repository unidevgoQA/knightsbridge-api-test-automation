import allure
from api.common_api import Api
from test_data.common_data.data import new_fee


@allure.step("Verify that user can not update fee with PUT request without token")
def test_common_settings_get_no_token_request():
    api = Api("common/settings")
    result = api.put_request(new_fee)
    status_code = result['status_code']
    assert status_code == 401
