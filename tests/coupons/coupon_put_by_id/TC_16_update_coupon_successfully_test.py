import allure
from api.common_api import Api
from test_data.coupons.data import random_coupon_id, update_coupon_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the coupon is updated successfully")
def test_coupon_updates_successfully():
    coupon_id_endpoint = "coupon/{}".format(random_coupon_id)
    coupon_api = Api(coupon_id_endpoint)
    result = coupon_api.put_request(payload=update_coupon_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
