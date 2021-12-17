import allure
from api.common_api import Api
from test_data.orders.data import order_id, order_status
from test_data.headers import headers_with_token


@allure.step("Verify that user can not update order by order id")
def test_update_order_fail():
    api_endpoint = "order/orderId/{}".format(order_id)
    order_api = Api(api_endpoint)
    result = order_api.patch_request(payload=order_status, headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 403
