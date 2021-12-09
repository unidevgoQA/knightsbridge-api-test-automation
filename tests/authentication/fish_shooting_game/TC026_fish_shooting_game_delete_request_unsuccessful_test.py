import allure
from api.common_api import Api


@allure.step("Fish Shooting Game Delete Request Unsuccessful Test")
def test_fish_shooting_delete_request_status():
    fish_api = Api("api/auth/game/fish-shooting-game")
    response = fish_api.delete_request()
    assert response['status_code'] == 404
