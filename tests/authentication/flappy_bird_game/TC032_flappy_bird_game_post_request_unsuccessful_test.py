import allure
from api.common_api import Api


@allure.step("Flappy Bird Game Post Request Unsuccessful Test")
def test_flappy_bird_game_request_status():
    fish_api = Api("api/auth/game/flappy-bird-game")
    response = fish_api.post_request()
    assert response['status_code'] == 404
