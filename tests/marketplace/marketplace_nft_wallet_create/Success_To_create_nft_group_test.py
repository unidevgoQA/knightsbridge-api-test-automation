import allure
from api.common_api import Api
from test_data.marketplace.data import *
from test_data.headers import admin_headers_with_token


@allure.step("All NFT Wallet Create Successfully")
def test_valid_nft_all_wallet_create():
    marketplace_group_api = Api("nft-wallet/all")
    result = marketplace_group_api.post_request(nft_wallet_all, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201


