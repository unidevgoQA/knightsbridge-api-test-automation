import allure
from api.common_api import Api
from test_data.reward.reward_data.data import new_badge
from test_data.headers import admin_headers_with_token

@allure.step("Verify create badge success")

def test_badge_create():
    badge_create_api = Api("badge/create")
    result = badge_create_api.post_request(new_badge, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201