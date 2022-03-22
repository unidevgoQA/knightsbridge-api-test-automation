import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_except_tokenId
from test_data.headers import admin_headers_with_token


@allure.step("Can not create NFT")
def test_failed_create_nft():
    marketplace_api = Api("market/create")
    result = marketplace_api.post_request(nft_create_except_tokenId, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
