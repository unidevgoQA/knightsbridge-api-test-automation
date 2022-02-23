import allure
from api.common_api import Api
from test_data.marketplace.data import nft_get_all_params
from test_data.headers import admin_headers_with_token


@allure.step("Verify that the user can get all nft")
def test_nft_get_all_valid():
    nft_type_endpoint = "marketplace?minPrice={}&maxPrice={}&category={}".format(nft_get_all_params['minPrice'],
                                                                                   nft_get_all_params['maxPrice'],
                                                                                   nft_get_all_params['category'])
    nft_api = Api(nft_type_endpoint)
    result = nft_api.get_request(payload=nft_get_all_params, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
