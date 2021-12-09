import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify dashboard games status code successful test")
def test_games_status_dashboard():
    games_api = Api("api/dashboard/games")
    response = games_api.send(headers=headers_with_token)
    assert response['status_code'] == 201
