import allure
from api.common_api import Api
from test_data.promotion.data import new_promotion_data


@allure.step("Verify create promotion by no token fail test")
def test_not_create_promotion_without_token():
    promotion_api = Api("promotion/create")
    result = promotion_api.post_request(payload=new_promotion_data)
    status_code = result['status_code']
    assert status_code == 401
