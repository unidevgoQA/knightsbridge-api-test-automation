import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_only_isAssignableToUser
from test_data.headers import admin_headers_with_token


@allure.step("NFT Should not Create with Only isAssignableToUser")
def test_nft_create_only_isAssignableToUser():
    nft_api = Api("marketplace/create")
    result = nft_api.post_request(nft_create_only_isAssignableToUser, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


