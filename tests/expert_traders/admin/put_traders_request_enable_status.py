import allure
from api.common_api import Api
from test_data.expert_trader.data import request_body
from test_data.headers import admin_headers_with_token

@allure.step('Verify enable trader req status')
def test_update_trader_request_status():
    # traders_request_api = Api('copyExperts/Pending')
    # result = traders_request_api.get_request(headers=admin_headers_with_token)
    # enable_status_update = result['response']['data'][0]
    api_endpoint = Api('copyExperts/enableStatus/{}'.format('trader_userid'))
    # traders_request_api = Api(api_endpoint)
    result = api_endpoint.put_request(payload=request_body,
                                             headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
