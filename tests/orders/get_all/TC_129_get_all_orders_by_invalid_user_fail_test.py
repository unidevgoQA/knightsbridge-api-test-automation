import allure
from api.common_api import Api
from test_data.orders.data import user_id_invalid
from test_data.headers import headers_with_token


@allure.step("Verify user can not get all orders by invalid user id")
def test_get_all_orders_by_user_id():
    api_endpoint = "order/get-all-user-orders/{}".format(user_id_invalid)
    order_api = Api(api_endpoint)
    result = order_api.get_request(headers=headers_with_token)
    status_code = result['status_code']
    assert status_code == 404
