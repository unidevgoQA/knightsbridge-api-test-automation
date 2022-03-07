import allure
from api.common_api import Api
from test_data.marketplace.data import nft_group_id, nft_group_invalid_id, nft_group_update
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the NFT group is updated successfully")
def test_nft_group_updates_successfully():
    nft_id_endpoint = "marketplace/group/{}".format(nft_group_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.put_request(payload=nft_group_update, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

