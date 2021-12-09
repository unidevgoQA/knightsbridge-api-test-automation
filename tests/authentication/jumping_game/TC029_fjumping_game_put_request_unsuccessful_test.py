import allure
from api.common_api import Api


@allure.step("Jumping game put request unsuccessful test")
def test_jumping_game_put_request_status():
    fish_api = Api("api/auth/game/jumping-game")
    response = fish_api.put_request()
    assert response['status_code'] == 400
