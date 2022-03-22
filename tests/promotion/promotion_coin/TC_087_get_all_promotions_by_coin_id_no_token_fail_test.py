import allure
from api.common_api import Api
from test_data.promotion.data import coin_id
from test_data.headers import headers_with_token


@allure.step("Verify that without user token retrieve promotion is not possible by coin id")
def test_get_all_promotions_by_coin_id_no_token():
    api_endpoint = "promotion/coin/{}".format(coin_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request()
    status_code = result['status_code']
    assert status_code == 401

