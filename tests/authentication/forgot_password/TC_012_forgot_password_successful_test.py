import allure
from api.user_api import UserApi
from test_data.user_data.data import only_valid_email


@allure.step('Forgot password successful test')
def test_forgot_password_successful():
    user_api = UserApi("api/users/forgot-password")
    result = user_api.post_request(only_valid_email)
    response = result["status_code"]
    assert response == 201
