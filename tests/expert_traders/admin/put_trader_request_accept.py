import allure
from api.common_api import Api
from test_data.expert_trader.data import request_body
from test_data.headers import admin_headers_with_token

@allure.step('Verify trader req accept status')
def test_accept_trader_request_status():

    api_endpoint = Api('copyExperts/{}'.format('trader_userid'))
    result = api_endpoint.put_request(payload=request_body, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
