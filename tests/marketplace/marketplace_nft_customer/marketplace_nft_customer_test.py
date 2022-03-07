import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_all_params
from test_data.headers import admin_headers_with_token, headers_with_token


@allure.step("Can not get nft without login.")
def test_invalid_nft_buy_get():
    marketplace_group_api = Api("marketplace/nft/customer")
    result = marketplace_group_api.get_request()
    status_code = result['status_code']
    print(status_code)
    assert status_code == 401


@allure.step("Authorized user can get the customer NFT")
def test_valid_nft_buy_get():
    marketplace_group_api = Api("marketplace/nft/customer")
    result = marketplace_group_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 200