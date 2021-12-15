import allure
from api.common_api import Api
from test_data.fiat.data import new_deposit
from test_data.headers import headers_with_token


@allure.step("Verify fiat deposit by user fail test")
def test_deposit_money():
    coupon_api = Api("fiat/deposit")
    result = coupon_api.post_request(new_deposit, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


