import allure
from api.common_api import Api
from test_data.coupons.data import new_coupon
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can't create Coupon with GET request")
def test_create_coupon_fail_get_request():
    coupon_create_api = Api("coupon/create")
    result = coupon_create_api.get_request(new_coupon, admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 500