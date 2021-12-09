import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Test no token unsuccessful test")
def test_no_token_dashboard_games():
    games_api = Api("api/dashboard/games")
    response = games_api.send(headers=headers)
    assert response['status_code'] == 201
