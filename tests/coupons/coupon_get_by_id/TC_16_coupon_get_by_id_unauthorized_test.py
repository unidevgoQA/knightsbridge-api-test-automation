import allure
from api.common_api import Api
from test_data.coupons.data import coupon_id
from test_data.headers import headers_with_token


@allure.step("Verify that the coupon is returned for unauthorized user")
def test_get_coupon_by_id():
    coupon_id_endpoint = "coupon/{}".format(coupon_id)
    coupon_api = Api(coupon_id_endpoint)
    result = coupon_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
