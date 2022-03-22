import allure
from api.common_api import Api


@allure.step("Verify that the status code is 200 of testcmc")
def test_test_cmc_get():
    coin_api = Api("coin/testCmc")
    result = coin_api.get_request_status()
    status_code = result.status_code
    assert status_code == 200
