import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.game_data.data import game_id_1


@allure.step("Verify games by id successful status test")
def test_games_with_ids():
    url = "api/dashboard/games/all-games/id/{}".format(game_id_1)
    games_api = Api(url)
    response = games_api.get_request_status(headers=headers_with_token)
    assert response.status_code == 200
