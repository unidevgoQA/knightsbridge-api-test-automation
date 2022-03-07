import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_by_id, update_nft_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the NFT is updated successfully")
def test_nft_updates_successfully():
    nft_id_endpoint = "marketplace/{}".format(nft_get_by_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.put_request(payload=update_nft_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
