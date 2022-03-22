import allure
from api.common_api import Api
from test_data.fiat.data import fiat_search


@allure.step("Verify fiat deposit get path args success test")
def test_get_deposit():
    endpoint = "fiat/deposit?pageSize={}&pageNumber={}&search={}&userId={}".format(
        fiat_search["pageNumber"],
        fiat_search["pageSize"],
        fiat_search["search"],
        fiat_search["userId"],
    )
    coupon_api = Api(endpoint)
    result = coupon_api.get_request(fiat_search)
    status_code = result['status_code']
    assert status_code == 401


