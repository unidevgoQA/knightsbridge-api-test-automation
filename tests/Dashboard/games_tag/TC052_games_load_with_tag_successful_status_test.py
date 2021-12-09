import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.game_data.data import action_tag


@allure.step("Verify games load with tag successful status code test")
def test_games_with_tags_status():
    url = "api/dashboard/games/tag/{}".format(action_tag)
    games_api = Api(url)
    response = games_api.get_request(headers=headers_with_token)
    assert response['status_code'] == 200
