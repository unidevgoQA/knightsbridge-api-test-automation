import allure
from api.common_api import Api
from test_data.coupons.data import new_coupon


@allure.step("Validate unauthorized user can not create coupon")
def test_valid_coupon_create():
    coupon_api = Api("coupon/create")
    result = coupon_api.post_request(new_coupon)
    status_code = result['status_code']
    assert status_code == 401
