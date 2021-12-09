import allure
from api.common_api import Api


@allure.step("Verify that user can't get game with put request")
def test_games_user_with_put_request_status():
    games_api = Api("api/dashboard/games/user")
    response = games_api.put_request()
    assert response['status_code'] == 400

