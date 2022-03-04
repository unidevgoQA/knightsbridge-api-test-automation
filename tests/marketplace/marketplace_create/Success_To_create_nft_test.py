import allure
from api.common_api import Api
from test_data.marketplace.data import new_nft
from test_data.headers import admin_headers_with_token


@allure.step("NFT Create successfully with authorized user")
def test_valid_nft_create():
    marketplace_api = Api("marketplace/create")
    result = marketplace_api.post_request(new_nft, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
