import allure
from api.common_api import Api
from test_data.marketplace.data import nft_buy
from test_data.headers import headers_with_token


@allure.step("NFT buy create successfully with authorized user")
def test_valid_nft_buy_create():
    marketplace_group_api = Api("marketplace/buy")
    result = marketplace_group_api.post_request(nft_buy, headers=headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 201
