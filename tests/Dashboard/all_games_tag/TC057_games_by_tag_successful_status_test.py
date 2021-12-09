import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.game_data.data import action_tag


@allure.step("Verify games by tag successful status test")
def test_all_games_by_tag():
    url = "api/dashboard/games/all-games/tag/{}".format(action_tag)
    games_api = Api(url)
    response = games_api.get_request_status(headers=headers_with_token)
    assert response.status_code == 200
