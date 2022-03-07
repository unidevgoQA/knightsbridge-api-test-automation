import allure
from api.common_api import Api
from test_data.marketplace.data import nft_buy_invalid_userId
from test_data.headers import headers_with_token


@allure.step("Can not buy NFT with invalid UserID")
def test_valid_nft_buy_create():
    marketplace_group_api = Api("marketplace/buy")
    result = marketplace_group_api.post_request(nft_buy_invalid_userId, headers=headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 403
