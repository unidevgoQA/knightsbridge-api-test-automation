import allure
from api.common_api import Api
from test_data.orders.data import new_order_data


@allure.step("Verify order creates unsuccessful with no token")
def test_order_create_no_token():
    order_api = Api("order/create")
    result = order_api.post_request(payload=new_order_data)
    status_code = result['status_code']
    assert status_code == 401
