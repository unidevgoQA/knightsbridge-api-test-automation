import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_only_tokenId
from test_data.headers import admin_headers_with_token


@allure.step("NFT Should not Create with Only tokenId")
def test_nft_create_only_tokenId():
    nft_api = Api("marketplace/create")
    result = nft_api.post_request(nft_create_only_tokenId, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


