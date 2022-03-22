import allure
from api.common_api import Api
from test_data.headers import headers_with_token


@allure.step("Verity no news returns without token")
def test_common_news_no_token_get_request():
    api = Api("common/news")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401
