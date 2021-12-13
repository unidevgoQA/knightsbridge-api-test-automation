import allure
from api.common_api import Api
from test_data.orders.data import user_id
from test_data.headers import headers_with_token


@allure.step("Verify user can get all orders by user")
def test_get_all_orders_by_user():
    api_endpoint = "order/get-all-user-orders/{}".format(user_id)
    order_api = Api(api_endpoint)
    result = order_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    message = result['response']['message']
    assert status_code == 401
    assert message == "Orders retrieved successfully"
