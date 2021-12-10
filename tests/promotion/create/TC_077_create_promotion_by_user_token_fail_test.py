import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.promotion.data import new_promotion_data


@allure.step("Verify can't create promotion by user token fail test")
def test_not_create_promotion():
    promotion_api = Api("promotion/create")
    result = promotion_api.post_request(payload=new_promotion_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
