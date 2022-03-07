import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_group_only_name
from test_data.headers import admin_headers_with_token


@allure.step("NFT Group should not Create with Only Name")
def test_nft_create_only_name():
    group_api = Api("marketplace/group")
    result = group_api.post_request(nft_create_group_only_name, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


