import allure
from test_data.user_data.data import invalid_user_data
from api.user_api import UserApi


@allure.step('Verify invalid credientials status code')
def test_invalid_sign_in_status_code():
    user_api = UserApi("api/users/signin")
    result = user_api.sign_in_user(invalid_user_data)
    message = result["response"]["error"]
    assert message == "User does not exist"

