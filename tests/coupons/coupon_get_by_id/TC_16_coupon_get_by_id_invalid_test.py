import allure
from api.common_api import Api
from test_data.coupons.data import invalid_coupon_id
from test_data.headers import headers_with_token


@allure.step("Verify that the coupon is not returned by the invalid id")
def test_get_coupon_by_id():
    coupon_id_endpoint = "coupon/{}".format(invalid_coupon_id)
    coupon_api = Api(coupon_id_endpoint)
    result = coupon_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 500
