import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.current_user_id import current_user_id


@allure.step("Verify get transaction information by admin in path")
def test_transactions_for_admin():
    api_endpoint = "transaction/{}".format(current_user_id)
    status_api = Api(api_endpoint)
    result = status_api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
