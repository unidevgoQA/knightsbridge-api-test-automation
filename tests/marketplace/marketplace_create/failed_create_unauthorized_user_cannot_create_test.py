import allure
from api.common_api import Api
from test_data.marketplace.data import new_nft


@allure.step("Validate unauthorized user can not create NFT")
def test_valid_coupon_create():
    coupon_api = Api("marketplace/create")
    result = coupon_api.post_request(new_nft)
    status_code = result['status_code']
    assert status_code == 401
