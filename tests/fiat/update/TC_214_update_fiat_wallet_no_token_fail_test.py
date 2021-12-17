import allure
from api.common_api import Api
from test_data.fiat.data import update_fiat, status, fiat_id


@allure.step("Verify that user can't update wallet no token")
def test_update_deposit_fail():
    coupon_api = Api("deposit/deposit/update/{}/{}".format(fiat_id, status))
    result = coupon_api.post_request(update_fiat)
    status_code = result['status_code']
    assert status_code == 404


