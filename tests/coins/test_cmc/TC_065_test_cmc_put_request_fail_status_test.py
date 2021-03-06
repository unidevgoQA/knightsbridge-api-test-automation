import allure
from api.common_api import Api


@allure.step("Verify that the status code is 400 of put cmc request no token")
def test_test_cmc_put_reqeust():
    coin_api = Api("coin/testCmc")
    result = coin_api.put_request()
    status_code = result['status_code']
    assert status_code == 401
