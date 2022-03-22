import allure
from api.common_api import Api
from test_data.promotion.data import coin_id
from test_data.headers import headers_with_token


@allure.step("Verify get all promotions by coin id user token success test")
def test_get_all_promotions_by_coin_id_user():
    api_endpoint = "promotion/coin/{}".format(coin_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    message = result['response']['message']
    assert status_code == 200
    assert message == "Promotions retrieved successfully"

