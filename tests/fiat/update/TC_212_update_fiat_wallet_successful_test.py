import allure
from api.common_api import Api
from test_data.fiat.data import update_fiat, status, fiat_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can update deposit")
def test_update_deposit():
    coupon_api = Api("deposit/deposit/update/{}/{}".format(fiat_id, status))
    result = coupon_api.post_request(update_fiat, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


