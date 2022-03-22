from random import choice
from api.common_api import Api
from test_data.headers import admin_headers_with_token

api = Api('marketplace/')
result = api.get_request(headers=admin_headers_with_token)
random_nft_id = choice(result['response']['data'])['_id']

new_nft = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

create_invalid_nft = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "Waterfall",
  "description": "An amazing view",
  "price": -90,
  "quantity": -23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "string",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}


nft_id_to_update = "621365a0bfed6f0027c6b1c0"

nft_invalid_id_to_update = "5465489846516489485"

nft_to_search = "Test NFT"

nft_get_by_id = {
  "id": "62146fb557c6fb00234bf15e"
}

nft_delete_by_id = {
  "id": "621365a0bfed6f0027c6b1c0"
}

nft_get_all_params = {
  "minPrice": "1",
  "maxPrice": "50",
  "category": "art"
}

update_nft_data = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "Waterfall",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "00039153bc5821105e760239378",
  "contractAddress": "0000x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "458554",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_only_image = {
    "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg"
}

nft_create_only_name = {

  "name": "Waterfall"
}

nft_create_only_description = {

  "description": "An amazing view"
}

nft_create_only_price = {
  "price": 90
}

nft_create_only_quantity = {
  "quantity": 23
}

nft_create_only_category = {

  "category": "art"
}

nft_create_only_tokenId = {

  "tokenId": "39153bc5821105e760239378"
}

nft_create_only_contractAddress = {
  "contractAddress": "0x226f9h6786811"
}

nft_create_only_tokenStandard = {

  "tokenStandard": "ERC-115"
}

nft_create_only_blockchain = {

  "blockchain": "Ethereum"
}

nft_create_only_metadata = {
  "metadata": "abcedser"
}

nft_create_only_isAssignableToUser = {
  "isAssignableToUser": True
}

nft_create_only_isVisibleInMarketplace = {
  "isVisibleInMarketplace": True
}

nft_create_only_isSold = {

  "isSold": False
}

nft_create_except_image ={
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_name = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_description = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_price = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_quantity = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_category = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_tokenId = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_contractAddress = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_tokenStandard = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_blockchain = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_metadata = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_isAssignableToUser = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isVisibleInMarketplace": True,
  "isSold": False
}

nft_create_except_isVisibaleInMarketplace = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isSold": False
}

nft_create_except_isSold = {
  "image": "https://storage.knights.app/kb-promotions-development/267280fee44981ea9619689f80c07672.jpg",
  "name": "UnidevGO Test NFT",
  "description": "An amazing view",
  "price": 90,
  "quantity": 23,
  "category": "art",
  "tokenId": "39153bc5821105e760239378",
  "contractAddress": "0x226f9h6786811",
  "tokenStandard": "ERC-115",
  "blockchain": "Ethereum",
  "metadata": "abcedser",
  "ownerId": "61993bc5821092e76023934a",
  "isAssignableToUser": True,
  "isVisibleInMarketplace": True
}






