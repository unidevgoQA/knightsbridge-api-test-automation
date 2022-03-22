import allure
from api.common_api import Api
from test_data.fiat.data import fiat_withdraw


@allure.step("Verify that user can not withdraw fiat wallet without token")
def test_():
    fiat_api = Api("fiat/withdraw")
    result = fiat_api.post_request(fiat_withdraw)
    status_code = result['status_code']
    assert status_code == 401
