import allure
from api.common_api import Api


@allure.step("Verify that the status code is 400 of delete cmc request")
def test_test_cmc_delete_reqeust():
    coin_api = Api("coin/testCmc")
    result = coin_api.delete_request()
    status_code = result['status_code']
    assert status_code == 401
