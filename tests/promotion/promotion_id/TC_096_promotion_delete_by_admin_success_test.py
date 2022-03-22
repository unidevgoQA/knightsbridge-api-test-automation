import allure
from api.common_api import Api
from test_data.promotion.data import new_promotion_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify promotion deletes successfully by admin test")
def test_promotion_deletes_by_admin_id():
    """
    First create a promotion and then delete it.
    """
    promotion_api = Api("promotion/create")
    result = promotion_api.post_request(new_promotion_data, headers=admin_headers_with_token)
    promotion_id = result['response']['data']['_id']
    delete_api_endpoint = "promotion/{}".format(promotion_id)
    delete_api = Api(delete_api_endpoint)
    delete_result = delete_api.delete_request(headers=admin_headers_with_token)
    status_code = delete_result['status_code']
    assert status_code == 200
