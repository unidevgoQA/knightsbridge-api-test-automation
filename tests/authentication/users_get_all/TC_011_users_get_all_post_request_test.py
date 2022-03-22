import allure
from api.user_api import UserApi


@allure.step('Verify no users return with post request')
def test_verify_no_user_with_post_request():
    user_api = UserApi("api/users/get-all")
    result = user_api.post_request()
    response = result["status_code"]
    assert response == 404
