import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verify that user can't get game with post request")
def test_games_user_with_post_request_status():
    games_api = Api("api/dashboard/games/user")
    response = games_api.post_request(headers=headers_with_token)
    assert response['status_code'] == 404

