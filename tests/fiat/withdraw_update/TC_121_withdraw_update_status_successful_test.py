import allure
from api.common_api import Api
from test_data.fiat.data import confirmed_status, user_id
from test_data.headers import headers_with_token


@allure.step("Verify withdraw status update successful test")
def test_update_withdraw():
    api_endpoint = "fiat/withdraw/update/{}/{}".format(user_id, confirmed_status)
    fiat_api = Api(api_endpoint)
    result = fiat_api.put_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


