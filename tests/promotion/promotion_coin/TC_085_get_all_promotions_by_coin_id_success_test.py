import allure
from api.common_api import Api
from test_data.promotion.data import coin_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify get all promotions by coin id success test")
def test_get_all_promotions_by_coin_id():
    api_endpoint = "promotion/coin/{}".format(coin_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    message = result['response']['message']
    assert status_code == 200
    assert message == "Promotions retrieved successfully"

