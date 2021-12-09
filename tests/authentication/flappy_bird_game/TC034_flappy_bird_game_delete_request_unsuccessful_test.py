import allure
from api.common_api import Api


@allure.step("Test flappy bird game Delete request unsuccessful test")
def test_jumping_game_delete_request_status():
    fish_api = Api("api/auth/game/flappy-bird-game")
    response = fish_api.delete_request()
    assert response['status_code'] == 404
