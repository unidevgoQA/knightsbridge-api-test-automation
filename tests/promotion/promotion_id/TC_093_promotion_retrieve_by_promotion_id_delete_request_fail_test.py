import allure
from api.common_api import Api
from test_data.promotion.data import promotion_id
from test_data.headers import headers_with_token


@allure.step("Verify promotion retrieve by promotion id delete request fail test")
def test_retrieve_promotion_by_promotion_id_delete_request():
    api_endpoint = "promotion/{}".format(promotion_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.post_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404

