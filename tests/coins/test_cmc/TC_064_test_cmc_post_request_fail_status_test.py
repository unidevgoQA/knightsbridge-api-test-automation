import allure
from api.common_api import Api


@allure.step("Verify that the status code is 400 of post cmc request")
def test_test_cmc_post_reqeust():
    coin_api = Api("coin/testCmc")
    result = coin_api.post_request()
    status_code = result['status_code']
    assert status_code == 404
