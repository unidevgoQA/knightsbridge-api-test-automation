import allure
from api.common_api import Api
from test_data.promotion.data import new_promotion_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that user can create promotion successfully")
def test_create_promotion():
    promotion_api = Api("promotion/create")
    result = promotion_api.post_request(new_promotion_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    assert result['response']['message'] == "Promotion added successfully"
