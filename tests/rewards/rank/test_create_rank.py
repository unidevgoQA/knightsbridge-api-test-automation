import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token
from test_data.reward.rank_data.data import new_rank
from test_data.reward.reward_data.data import new_reward_no_goal, new_reward, \
    new_reward_no_start_date, \
    new_reward_no_end_date, \
    new_reward_no_events


@allure.step("Validate user is able to create reward successfully")
def test_create_reward_valid():
    reward = Api("reward/create")
    result = reward.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201


@allure.step("Validate user is not able to create reward without goalname")
def test_create_reward_no_goal():
    reward = Api("reward/create")
    result = reward.post_request(new_reward_no_goal, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without start date")
def test_create_reward_no_start_date():
    reward = Api("reward/create")
    result = reward.post_request(new_reward_no_start_date, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without end date")
def test_create_reward_no_end_date():
    reward = Api("reward/create")
    result = reward.post_request(new_reward_no_end_date, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without events")
def test_create_reward_no_events():
    reward = Api("reward/create")
    result = reward.post_request(new_reward_no_events, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward with get request")
def test_create_reward_get():
    reward = Api("reward/create")
    result = reward.get_request(new_reward, headers=admin_headers_with_token)
    message = result['response']['message']
    assert message is "Internal server error"


@allure.step("Validate user is not able to create reward with put request")
def test_create_reward_put():
    reward = Api("reward/create")
    result = reward.put_request(new_reward, headers=admin_headers_with_token)
    message = result['response']['message']
    assert message == "Internal server error"

# @allure.step("Validate user is able to create rank successfully")
# def test_create_rank_valid():
#     rank_api = Api("reward/rank")
#     result = rank_api.post_request(new_rank, headers=admin_headers_with_token)
#     status_code = result['status_code']
#     assert status_code == 201
