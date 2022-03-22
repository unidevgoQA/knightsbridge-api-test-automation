import allure
from api.user_api import UserApi


@allure.step('Get all users successfully')
def test_verify_empty_password_sign_in():
    user_api = UserApi("api/users/get-all")
    result = user_api.get_request()
    response = result["status_code"]
    assert response == 200
