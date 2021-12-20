import allure
from api.common_api import Api
from test_data.fiat.data import new_deposit
from test_data.headers import admin_headers_with_token


@allure.step("Verify fiat deposit get request fail test")
def test_deposit_money():
    coupon_api = Api("fiat/deposit")
    result = coupon_api.put_request(new_deposit, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


