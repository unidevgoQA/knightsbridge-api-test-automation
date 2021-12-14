import allure
from api.common_api import Api
from test_data.crypto_wallet.data import retrieve_by_uid_coin_id_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify retrieve crypto wallet fail by uid and coin id test")
def test_retrieve_wallet_by_uid_coin_id():
    api_endpoint = "cryptoWallet?userId={0}&coinId={1}".\
        format(retrieve_by_uid_coin_id_data["userId"], retrieve_by_uid_coin_id_data["coinId"])
    crypto_api = Api(api_endpoint)
    result = crypto_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
