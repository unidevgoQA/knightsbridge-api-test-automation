import allure
from api.common_api import Api
from test_data.coupons.data import new_coupon
from test_data.headers import admin_headers_with_token


@allure.step("Coupon Create successfully with authorized user")
def test_valid_coupon_create():
    coupon_api = Api("coupon/create")
    result = coupon_api.post_request(new_coupon, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
