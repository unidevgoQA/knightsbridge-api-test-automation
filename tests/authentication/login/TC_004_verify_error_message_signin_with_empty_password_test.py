import allure
from test_data.user_data.data import empty_password_data
from api.user_api import UserApi


@allure.step('Verify error message signin with empty password')
def test_verify_empty_password_sign_in():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(empty_password_data)
    response = result["status_code"]
    assert response == 401



