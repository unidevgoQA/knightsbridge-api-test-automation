import allure
from api.common_api import Api
from test_data.coupons.data import coupon_id_to_update, update_coupon_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the coupon is not updated successfully")
def test_coupon_updates_successfully():
    coupon_id_endpoint = "coupon/{}".format(coupon_id_to_update)
    coupon_api = Api(coupon_id_endpoint)
    result = coupon_api.put_request(update_coupon_data)
    status_code = result['status_code']
    assert status_code == 401
