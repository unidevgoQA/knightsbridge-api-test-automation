import allure
from api.common_api import Api
from test_data.marketplace.data import nft_buy
from test_data.headers import admin_headers_with_token


@allure.step("Failed to Create NFT buy")
def test_buy_nft_create():
    marketplace_group_api = Api("marketplace/buy")
    result = marketplace_group_api.post_request(nft_buy)
    status_code = result['status_code']
    assert status_code == 401
