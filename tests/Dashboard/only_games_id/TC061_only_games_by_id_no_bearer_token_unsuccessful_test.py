import allure
from api.common_api import Api
from test_data.headers import headers
from test_data.game_data.data import game_id_1


@allure.step("Test Only Games By Id No Bearer Token Unsuccessful Test")
def test_only_games_with_ids_no_token_test():
    url = "api/dashboard/games/id/{}".format(game_id_1)
    games_api = Api(url)
    response = games_api.get_request_status(headers=headers)
    assert response.status_code == 401
