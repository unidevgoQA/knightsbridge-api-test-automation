import allure
from test_data.user_data.data import user_data_pass_length_less_than_6
from api.user_api import UserApi


@allure.step('Verify error message signin with password longer or eq 6 chr')
def test_verify_empty_password_sign_in():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(user_data_pass_length_less_than_6)
    response = result["status_code"]
    assert response == 401
