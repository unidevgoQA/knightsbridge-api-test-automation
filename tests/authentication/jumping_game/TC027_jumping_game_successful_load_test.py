import allure
from api.common_api import Api


@allure.step("Jumping game successful load test")
def test_jumping_game_success_status():
    fish_api = Api("api/auth/game/jumping-game")
    response = fish_api.get_request()
    assert response['status_code'] == 200
