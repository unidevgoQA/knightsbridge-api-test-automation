import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_group_except_icon
from test_data.headers import admin_headers_with_token


@allure.step("NFT Group should not Create with Except Icon")
def test_nft_group_create_except_icon():
    group_api = Api("marketplace/group")
    result = group_api.post_request(nft_create_group_except_icon, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400