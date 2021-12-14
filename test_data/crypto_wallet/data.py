from utils.read_update_counter import read_counter

new_crypto_wallet = {
  "userId": "0152123997001705569764{}".format(read_counter()),
  "coinId": "61b1d3de18ec7f2e0be39810",
  "quantity": 1,
  "reservedQuantity": 1
}

already_exists_user_id_in_crypto_wallet = '015212399700170556976483'

exist_wallet = {
  "userId": already_exists_user_id_in_crypto_wallet,
  "coinId": "61b1d3de18ec7f2e0be39810",
  "quantity": 1,
  "reservedQuantity": 1
}

update_crypto_wallet_data = {
  "userId": already_exists_user_id_in_crypto_wallet,
  "coinId": "61b1d3de18ec7f2e0be39810",
  "quantity": 5,
  "reservedQuantity": 2
}

crypto_wallet_id = "61a94aaa8df9eb001c195ef4"

retrieve_by_uid_coin_id_data = {
  "userId": already_exists_user_id_in_crypto_wallet,
  "coinId": "61b1d3de18ec7f2e0be39810",
}