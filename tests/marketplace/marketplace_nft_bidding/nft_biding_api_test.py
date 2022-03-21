import allure
from api.common_api import Api
from test_data.headers import headers_with_token, admin_headers_with_token
from test_data.marketplace.data import nft_bid_place, nft_bid_place_with_only_nftId, nft_bid_place_with_only_userId, nft_bid_place_with_only_bidPrice, nft_highest_bid


## API Endpoint: marketplace/nft/visible/dashboard

@allure.step("User should not be able to see NFT in the Dashboard")
def test_failed_to_get_nft():
    marketplace_dashboard_api = Api("marketplace/nft/visible/dashboard")
    result = marketplace_dashboard_api.get_request()
    status_code = result['status_code']
    print(result)
    assert status_code == 401


@allure.step("User should be able to see NFT in the Dashboard")
def test_get_nft_dashboard():
    marketplace_dashboard_api = Api("marketplace/nft/visible/dashboard")
    result = marketplace_dashboard_api.get_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 200



## API Endpoint: marketplace/get/nft-in-each-group

@allure.step("Unauthorised User should not get nft in each group")
def test_not_get_nft_in_each_group():
    api = Api("marketplace/get/nft-in-each-group")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("User should get nft in each group")
def test_get_nft_in_each_group():
    api = Api("marketplace/get/nft-in-each-group")
    result = api.get_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("User should not get nft in each group with Post method")
def test_not_get_nft_in_each_group_with_post_method():
    api = Api("marketplace/get/nft-in-each-group")
    result = api.post_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


## API Endpoint: marketplace/get/group/nft-count

@allure.step("Unauthorised User should not get nft count")
def test_not_get_nft_count():
    api = Api("marketplace/get/group/nft-count")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("User should get nft count")
def test_get_nft_count():
    api = Api("marketplace/get/group/nft-count")
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("User should not get nft count with post method")
def test_not_get_nft_count_with_post_method():
    api = Api("marketplace/get/group/nft-count")
    result = api.post_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404



## API Endpoint: marketplace/nfts/coins

@allure.step("Unauthorised User should not get nft coins")
def test_not_get_nft_coins():
    api = Api("marketplace/nfts/coins")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("User should get nft coins")
def test_get_nft_coins():
    api = Api("marketplace/nfts/coins")
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("User should not get nft coins with post method")
def test_not_get_nft_coins_with_post_method():
    api = Api("marketplace/nfts/coins")
    result = api.post_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


## API Endpoint: marketplace/bid/place

@allure.step("Unauthorized user can not  Post NFT Bid in the marketplace")
def test_invalid_nft_bid_create():
    marketplace_api = Api("marketplace/bid/place")
    result = marketplace_api.post_request(nft_bid_place)
    status_code = result['status_code']
    assert status_code == 401

@allure.step("Successfully Post NFT Bid in the marketplace")
def test_valid_nft_bid_create():
    marketplace_api = Api("marketplace/bid/place")
    result = marketplace_api.post_request(nft_bid_place, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 201

@allure.step("Failed to  Post NFT Bid in the marketplace with only nft id ")
def test_failed_nft_bid_create_with_only_nftId():
    marketplace_api = Api("marketplace/bid/place")
    result = marketplace_api.post_request(nft_bid_place_with_only_nftId, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Failed to  Post NFT Bid in the marketplace with only user id")
def test_failed_nft_bid_create_with_only_userId():
    marketplace_api = Api("marketplace/bid/place")
    result = marketplace_api.post_request(nft_bid_place_with_only_userId, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 400

@allure.step("Failed to Post NFT Bid in the marketplace with only bidPrice")
def test_failed_nft_bid_create_with_only_bidPrice():
    marketplace_api = Api("marketplace/bid/place")
    result = marketplace_api.post_request(nft_bid_place_with_only_bidPrice, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 400

## API Endpoint: marketplace/highest-bid/{nftId}

@allure.step("Unauthorized User should not get nft highest bid")
def test_not_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("Authorized User should get nft highest bid")
def test_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("Authorized User should not get nft highest bid with post method")
def test_not_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.post_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 404

@allure.step("Authorized User should not get nft highest bid without putting NFT ID")
def test_not_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid"
    nft_api = Api(nft_id_endpoint)
    result = nft_api.post_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 404

## API Endpoint: marketplace/bids/all/{nftId}

@allure.step("Unauthorized User should not get bids all nft")
def test_not_get_bids_all_nft():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("Authorized User should get nft highest bid")
def test_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.get_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("Authorized User should not get nft highest bid with post method")
def test_not_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid/{}".format(nft_highest_bid)
    nft_api = Api(nft_id_endpoint)
    result = nft_api.post_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 404

@allure.step("Authorized User should not get nft highest bid without putting NFT ID")
def test_not_get_nft_highest_bid():
    nft_id_endpoint = "marketplace/highest-bid"
    nft_api = Api(nft_id_endpoint)
    result = nft_api.post_request(headers= headers_with_token)
    status_code = result['status_code']
    assert status_code == 404



## API Endpoint: marketplace/nft/all/highest-bid

@allure.step("Unauthorised User should not get all highest nft bid")
def test_not_get_highest_bid():
    api = Api("marketplace/nft/all/highest-bid")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401

@allure.step("Authorised User should get all highest nft bid")
def test_get_nft_highest_bid():
    api = Api("marketplace/nft/all/highest-bid")
    result = api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 200

@allure.step("Authorised User should not get all highest nft bid with post method")
def test_not_get_highest_bid():
    api = Api("marketplace/nft/all/highest-bid")
    result = api.post_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
