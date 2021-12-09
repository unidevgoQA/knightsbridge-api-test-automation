import allure
from api.common_api import Api


@allure.step("flappy_bird_game_successful_load_test")
def test_flappy_bird_game_success_status():
    fish_api = Api("api/auth/game/flappy-bird-game")
    response = fish_api.get_request()
    assert response['status_code'] == 200
