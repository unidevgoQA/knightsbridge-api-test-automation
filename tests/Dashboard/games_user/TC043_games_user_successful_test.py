import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify current user games")
def test_current_user_games():
    games_api = Api("api/dashboard/games/user")
    response = games_api.get_request(headers=headers_with_token)
    assert response['status_code'] == 200
    assert "games" in response['response']

