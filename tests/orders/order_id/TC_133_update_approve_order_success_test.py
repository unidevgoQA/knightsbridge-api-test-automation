import allure
from api.common_api import Api
from test_data.orders.data import order_id, approve_data
from test_data.headers import admin_headers_with_token


@allure.step("Verify approve order success")
def test_approve_order():
    api_endpoint = "order/approve/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.put_request(payload=approve_data, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
