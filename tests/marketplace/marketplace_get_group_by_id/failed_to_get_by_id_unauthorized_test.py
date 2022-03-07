import allure
from api.common_api import Api
from test_data.marketplace.data import nft_group_id
from test_data.headers import headers_with_token


@allure.step("Can not get Group by ID with unauthorized user")
def test_get_coupon_by_id():
    nft_id_endpoint = "marketplace/group{}".format(nft_group_id)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
