import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Verify error message returns without token")
def test_current_user_games():
    games_api = Api("api/dashboard/games/user")
    response = games_api.get_request(headers=headers)
    assert response['status_code'] == 401
    assert response['response']['message'] == "Unauthorized"

