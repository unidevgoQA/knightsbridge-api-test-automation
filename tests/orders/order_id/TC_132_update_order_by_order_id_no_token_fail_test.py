import allure
from api.common_api import Api
from test_data.orders.data import order_id, order_status


@allure.step("Verify that user can not update order by order id no token")
def test_update_order_fail_no_token():
    api_endpoint = "order/orderId/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.patch_request(payload=order_status)
    status_code = result['status_code']
    assert status_code == 401
