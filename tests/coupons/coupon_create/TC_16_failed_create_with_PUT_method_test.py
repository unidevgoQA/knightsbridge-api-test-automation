import allure
from api.common_api import Api
from test_data.coupons.data import new_coupon
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can't create Coupon with PUT request")
def test_valid_coupon_create():
    coupon_create_api = Api("coupon/create")
    result = coupon_create_api.put_request(new_coupon, admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400
