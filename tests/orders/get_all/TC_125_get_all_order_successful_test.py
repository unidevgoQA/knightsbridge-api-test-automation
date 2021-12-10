# import allure
# from api.common_api import Api
# from test_data.orders.data import get_all_orders_data
# from test_data.headers import headers_with_token
#
#
# @allure.step("Verify get all orders with for a user")
# def test_get_all_orders():
#
#     order_api = Api("order/get-all")
#     result = order_api.post_request(order_get_data_invalid_coin_id, headers=headers_with_token)
#     status_code = result['status_code']
#     assert status_code == 404  # failing because of insufficient balance could not place order
