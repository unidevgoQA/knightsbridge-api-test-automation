import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_group
from test_data.headers import admin_headers_with_token


@allure.step("NFT Group create successfully with authorized user")
def test_valid_nft_group_create():
    marketplace_group_api = Api("marketplace/group")
    result = marketplace_group_api.post_request(nft_create_group, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
