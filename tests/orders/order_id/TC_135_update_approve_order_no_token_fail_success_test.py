import allure
from api.common_api import Api
from test_data.orders.data import order_id, approve_data


@allure.step("Verify approve order fail no token")
def test_approve_order_no_token():
    api_endpoint = "order/approve/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.put_request(payload=approve_data)
    status_code = result['status_code']
    assert status_code == 401
