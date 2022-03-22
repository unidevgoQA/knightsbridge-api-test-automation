import allure
from api.common_api import Api
from test_data.fiat.data import fiat_search
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can not get deposit with put request")
def test_get_deposit():
    endpoint = "fiat/deposit?pageSize={}&pageNumber={}&search={}&userId={}".format(
        fiat_search["pageNumber"],
        fiat_search["pageSize"],
        fiat_search["search"],
        fiat_search["userId"],
    )
    coupon_api = Api(endpoint)
    result = coupon_api.put_request(fiat_search, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


