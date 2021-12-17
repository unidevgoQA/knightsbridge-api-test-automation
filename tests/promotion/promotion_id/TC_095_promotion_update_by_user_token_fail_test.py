import allure
from api.common_api import Api
from test_data.promotion.data import promotion_to_update
from test_data.headers import headers_with_token


@allure.step("Verify promotion update by user token fail test")
def test_promotion_update_by_user_token():
    api_endpoint = "promotion/{}".format(promotion_to_update['id'])
    promotion_api = Api(api_endpoint)
    result = promotion_api.put_request(payload=promotion_to_update,
                                       headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403

