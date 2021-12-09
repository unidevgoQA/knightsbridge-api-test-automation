import allure
from api.common_api import Api
from test_data.headers import headers
from test_data.game_data.data import game_id_1


@allure.step("Verify no games by id without token post request")
def test_games_with_ids_no_token_post_test():
    url = "api/dashboard/games/all-games/id/{}".format(game_id_1)
    games_api = Api(url)
    response = games_api.post_request(headers=headers)
    assert response['status_code'] == 404
