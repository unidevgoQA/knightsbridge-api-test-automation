import allure
from test_data.user_data.data import valid_user_data
from api.user_api import UserApi


@allure.step('Verify User Signed In Successfully status code test')
def test_success_user_sign_in():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(valid_user_data)
    response = result["status_code"]
    assert response == 201
