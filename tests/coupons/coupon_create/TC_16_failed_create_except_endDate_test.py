import allure
from api.common_api import Api
from test_data.coupons.data import coupon_create_except_endDate
from test_data.headers import admin_headers_with_token


@allure.step("Coupon Should not Create filling all mandatory fields except endDate")
def test_coupon_create_except_endDate():
    coupon_api = Api("coupon/create")
    result = coupon_api.post_request(coupon_create_except_endDate, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400
