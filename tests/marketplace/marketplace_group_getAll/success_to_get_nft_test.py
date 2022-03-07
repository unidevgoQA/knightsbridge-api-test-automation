import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_all_params
from test_data.headers import admin_headers_with_token


@allure.step("Authorized user can get the all  NFT Group")
def test_group_getall_authorized():
    marketplace_group_api = Api("marketplace/group/all")
    result = marketplace_group_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 401


@allure.step("Authorized user can get the all  NFT Group")
def test_group_getall_authorized():
    marketplace_group_api = Api("marketplace/group/all")
    result = marketplace_group_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 200
