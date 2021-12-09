import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Verify games with name loads successfully")
def test_games_with_names():
    url = "api/dashboard/games/name/{}".format("flappy-bird-game")
    games_api = Api(url)
    response = games_api.get_request(headers=headers)
    assert response['status_code'] == 401
