import allure
from api.common_api import Api
from test_data.orders.data import order_id, approve_data
from test_data.headers import headers_with_token


@allure.step("Verify approve order fail by user")
def test_approve_order_fail_user():
    api_endpoint = "order/approve/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.put_request(payload=approve_data, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
