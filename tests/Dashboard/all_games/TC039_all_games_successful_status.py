import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify all games api successful status code")
def test_all_games_success():
    games_api = Api("api/dashboard/games/all-games")
    response = games_api.get_request(headers=headers_with_token)
    assert response['status_code'] == 200
    assert response['response'][0]['name'] == "Jumping Game"
