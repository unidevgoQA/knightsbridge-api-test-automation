import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Verify unsuccessful return ut request status test")
def test_put_request_all_games():
    games_api = Api("api/dashboard/games/all-games")
    response = games_api.put_request()
    assert response['status_code'] == 400
