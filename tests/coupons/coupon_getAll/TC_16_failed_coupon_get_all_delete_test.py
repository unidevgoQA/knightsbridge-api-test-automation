import allure
from api.common_api import Api
from test_data.coupons.data import coupon_get_all_params
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the user can not get all coupon by delete request")
def test_coupon_get_all_valid():
    coupon_type_endpoint = "coupon/getAll?pageSize={}&pageNumber={}&search".format(coupon_get_all_params['pageSize'],
                                                                                   coupon_get_all_params['pageNumber'],
                                                                                   coupon_get_all_params['search'])
    coupon_api = Api(coupon_type_endpoint)
    result = coupon_api.delete_request(headers=admin_headers_with_token)
    message = result['response']['message']
    assert message == 'Internal server error'
