import allure
from api.common_api import Api
from test_data.headers import headers
from test_data.game_data.data import action_tag


@allure.step("Get all games by tag with no bearer token success")
def test_all_games_with_tags_no_token_test():
    url = "api/dashboard/games/all-games/tag/{}".format(action_tag)
    games_api = Api(url)
    response = games_api.get_request_status(headers=headers)
    assert response.status_code == 200
