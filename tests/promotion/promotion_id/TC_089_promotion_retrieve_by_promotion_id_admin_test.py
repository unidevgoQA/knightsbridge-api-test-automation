import allure
from api.common_api import Api
from test_data.promotion.data import random_promotion_id
from test_data.headers import admin_headers_with_token


@allure.step("Verify promotion retrieve by promotion id by admin test success")
def test_retrieve_promotion_by_promotion_id_by_admin():
    api_endpoint = "promotion/{}".format(random_promotion_id)
    promotion_api = Api(api_endpoint)
    result = promotion_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    message = result['response']['message']
    assert status_code == 200
    assert message == 'Promotion retrieved successfully'
