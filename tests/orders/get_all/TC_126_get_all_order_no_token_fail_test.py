import allure
from api.common_api import Api


@allure.step("Verify no orders returns without token")
def test_no_orders_return():
    order_api = Api("order/get-all")
    result = order_api.get_request()
    status_code = result['status_code']
    assert status_code == 401