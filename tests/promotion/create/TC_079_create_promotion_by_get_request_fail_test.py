import allure
from api.common_api import Api
from test_data.promotion.data import new_promotion_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can not create promotion by get request")
def test_not_create_promotion_with_get_request():
    promotion_api = Api("promotion/create")
    result = promotion_api.get_request(payload=new_promotion_data, headers=admin_headers_with_token)
    message = result['response']['message']
    assert message == "Internal server error"
