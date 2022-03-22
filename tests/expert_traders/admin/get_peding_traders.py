import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token

@allure.step("Verify that the admin can get pending expert traders")

def test_pending_traders_get_all_valid():
    traders_request_api = Api("copyExperts/Pending")
    result = traders_request_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

