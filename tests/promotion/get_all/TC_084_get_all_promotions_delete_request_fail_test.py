import allure
from api.common_api import Api
from test_data.promotion.data import promo_type_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can't get all promotions with delete request")
def test_get_all_promotions_by_delete_request_promo_type():
    api_endpoint = "promotion/get-all?promoType={}".format(promo_type_data['banner'])
    promotion_api = Api(api_endpoint)
    result = promotion_api.post_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
