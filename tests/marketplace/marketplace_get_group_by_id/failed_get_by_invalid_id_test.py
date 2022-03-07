import allure
from api.common_api import Api
from test_data.marketplace.data import nft_invalid_id_to_update
from test_data.headers import headers_with_token


@allure.step("Verify that the NFT  is not returned by the invalid id")
def test_get_coupon_by_id():
    nft_id_endpoint = "marketplace/{}".format(nft_invalid_id_to_update)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request(headers=headers_with_token)
    message = result['response']['message']

    assert message == 'Internal server error'
