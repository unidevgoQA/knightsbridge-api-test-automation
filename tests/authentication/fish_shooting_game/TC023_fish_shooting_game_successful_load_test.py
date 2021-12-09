import allure
from api.common_api import Api


@allure.step("Fish Shooting Game - Successful Load Test")
def test_fish_shooting_game_success_status():
    fish_api = Api("api/auth/game/fish-shooting-game")
    response = fish_api.get_request()
    assert response['status_code'] == 200
