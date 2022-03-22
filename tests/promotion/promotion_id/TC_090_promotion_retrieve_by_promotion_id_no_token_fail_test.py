import allure
from api.common_api import Api
from test_data.promotion.data import promotion_id


@allure.step("Verify promotion retrieve by promotion id no token fail test")
def test_retrieve_promotion_by_promotion_id_no_token():
    api_endpoint = "promotion/{}".format(promotion_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
