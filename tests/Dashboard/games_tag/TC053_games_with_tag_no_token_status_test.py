import allure
from api.common_api import Api
from test_data.headers import headers
from test_data.game_data.data import sport_tag


@allure.step("Verify games with tag no token status test")
def test_games_with_names():
    url = "api/dashboard/games/tag/{}".format(sport_tag)
    games_api = Api(url)
    response = games_api.get_request(headers=headers)
    assert response['status_code'] == 401
