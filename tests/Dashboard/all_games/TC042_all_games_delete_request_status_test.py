import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Verify that user can't delete game")
def test_delete_request_all_games():
    games_api = Api("api/dashboard/games/all-games")
    response = games_api.delete_request()
    assert response['status_code'] == 404
