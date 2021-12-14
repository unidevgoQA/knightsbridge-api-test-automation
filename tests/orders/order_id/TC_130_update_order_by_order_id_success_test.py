import allure
from api.common_api import Api
from test_data.orders.data import order_id, order_status
from test_data.headers import admin_headers_with_token


@allure.step("Verify that admin can update order by order id")
def test_update_order():
    api_endpoint = "order/orderId/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.patch_request(payload=order_status, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
