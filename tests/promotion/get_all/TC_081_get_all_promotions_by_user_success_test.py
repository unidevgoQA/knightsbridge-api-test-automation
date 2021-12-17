import allure
from api.common_api import Api
from test_data.promotion.data import promo_type_data
from test_data.headers import headers_with_token


@allure.step("Verify that user can get all promotions by type")
def test_get_all_promotions_by_promo_type():
    api_endpoint = "promotion/get-all?promoType={}".format(promo_type_data['banner'])
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
