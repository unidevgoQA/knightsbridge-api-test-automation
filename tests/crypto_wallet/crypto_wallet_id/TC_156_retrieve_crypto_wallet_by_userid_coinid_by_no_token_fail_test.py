import allure
from api.common_api import Api
from test_data.crypto_wallet.data import retrieve_by_uid_coin_id_data


@allure.step("Verify retrieve crypto wallet fail by no token test")
def test_retrieve_wallet_by_no_token():
    api_endpoint = "cryptoWallet?userId={0}&coinId={1}".\
        format(retrieve_by_uid_coin_id_data["userId"], retrieve_by_uid_coin_id_data["coinId"])
    crypto_api = Api(api_endpoint)
    result = crypto_api.get_request()
    status_code = result['status_code']
    assert status_code == 401
