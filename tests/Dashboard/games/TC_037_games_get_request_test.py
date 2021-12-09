import allure
from api.common_api import Api


@allure.step("Test games with get request unsuccessful")
def test_get_request_dashboard_games():
    games_api = Api("api/dashboard/games")
    response = games_api.get_request()
    assert response['status_code'] == 404
