import allure
from api.common_api import Api
from test_data.marketplace.data import nft_create_group
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the NFT Group is deleted")
def test_nft_group_deleted():
    nft_group_create_api = Api("marketplace/group")
    result = nft_group_create_api.post_request(nft_create_group, headers=admin_headers_with_token)
    nft_id = result['response']['data']['_id']
    nft_id_endpoint = "marketplace/group/{}".format(nft_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.delete_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
