import allure
from api.common_api import Api
from test_data.marketplace.data import new_nft
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the NFT is deleted")
def test_coupon_deletes_by_user():
    nft_create_api = Api("marketplace/create")
    result = nft_create_api.post_request(new_nft, headers=admin_headers_with_token)
    nft_id = result['response']['data']['_id']
    nft_id_endpoint = "marketplace/{}".format(nft_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.delete_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
