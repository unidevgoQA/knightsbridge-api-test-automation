import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_by_id
from test_data.headers import headers_with_token


@allure.step("Verify that the NFT  is returned by the valid id")
def test_get_coupon_by_id():
    nft_id_endpoint = "marketplace/{}".format(nft_get_by_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
