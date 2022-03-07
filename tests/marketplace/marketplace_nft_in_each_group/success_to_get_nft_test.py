import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_all_params
from test_data.headers import admin_headers_with_token



@allure.step("NFT in each group")
def test_nft_in_group():
    marketplace_group_api = Api("marketplace/get/nft-in-each-group")
    result = marketplace_group_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    print(status_code)
    assert status_code == 200
