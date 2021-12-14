import allure
from api.common_api import Api
from test_data.coupons.data import new_coupon
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the coupon is not deleted by get method")
def test_coupon_deletes_by_user():
    coupon_create_api = Api("coupon/create")
    result = coupon_create_api.post_request(new_coupon, headers=admin_headers_with_token)
    coupon_id = result['response']['data']['_id']
    coupon_id_endpoint = "coupon/{}".format(coupon_id)
    coin_api = Api(coupon_id_endpoint)
    result = coin_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
