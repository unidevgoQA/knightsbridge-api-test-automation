import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token, headers_with_token
from test_data.activity_log.data import new_activity_log, new_activity_log_no_event_name, \
    new_activity_log_no_email, \
    new_activity_log_no_amount, \
    new_activity_log_no_status

activity_log_create_api = Api("activity-log")


@allure.step("Validate user is able to create new activity log successfully")
def test_create_new_activity_log():
    response = activity_log_create_api.post_request(new_activity_log, headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 201


@allure.step("Validate activity creation fails without event name")
def test_create_new_activity_log_without_event_name():
    response = activity_log_create_api.post_request(new_activity_log_no_event_name, headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 400


@allure.step("Validate activity log creation fails with user token")
def test_create_new_activity_log_without_user_email():
    response = activity_log_create_api.post_request(new_activity_log_no_email, headers=headers_with_token)
    status_code = response['status_code']
    assert status_code == 403


@allure.step("Validate activity logs doesn't create without email")
def test_create_new_activity_log_without_email():
    response = activity_log_create_api.post_request(new_activity_log_no_email, headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 400


@allure.step("Validate activity log creation fails without amount")
def test_create_new_activity_log_without_amount():
    response = activity_log_create_api.post_request(new_activity_log_no_amount, headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 400


@allure.step("Validate activity log creation fails without status")
def test_create_new_activity_log_without_status():
    response = activity_log_create_api.post_request(new_activity_log_no_status, headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 400


@allure.step("Validate activity logs can be retrieved successfully by admin")
def test_get_all_activity_logs():
    response = activity_log_create_api.get_request(headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 200


@allure.step("Validate activity logs can not be retrieved by user")
def test_get_all_activity_logs_by_user():
    response = activity_log_create_api.get_request(headers=headers_with_token)
    status_code = response['status_code']
    assert status_code == 403


@allure.step("Validate activity logs can be retrieved by sizing")
def test_get_all_activity_logs_by_sizing():
    api = Api("activity-log?pageSize={}pageNumber={}".format(1, 1))
    response = api.get_request(headers=admin_headers_with_token)
    status_code = response['status_code']
    assert status_code == 200
