import allure
from api.common_api import Api
from test_data.promotion.data import promotion_to_update
from test_data.headers import admin_headers_with_token


@allure.step("Verify promotion update by promotion id success")
def test_promotion_update_by_promotion_id():
    api_endpoint = "promotion/{}".format(promotion_to_update['id'])
    promotion_api = Api(api_endpoint)
    result = promotion_api.put_request(payload=promotion_to_update,
                                       headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

