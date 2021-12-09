import allure
from api.common_api import Api
from test_data.headers import headers


@allure.step("Verify no games returned without bearer token")
def test_all_games_no_token():
    games_api = Api("api/dashboard/games/all-games")
    response = games_api.get_request(headers=headers)
    assert response['status_code'] == 401
    assert response['response']['message'] == 'Could not find your Account'
