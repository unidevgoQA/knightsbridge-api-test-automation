import allure
from api.common_api import Api
from test_data.promotion.data import promo_type_data


@allure.step("Verify that user can not get all promotions by type status 401")
def test_no_get_all_promotions_by_promo_type():
    api_endpoint = "promotion/get-all?promoType={}".format(promo_type_data['banner'])
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
