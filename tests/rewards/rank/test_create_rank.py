import allure
from api.common_api import Api
from test_data.headers import admin_headers_with_token, user_token
from test_data.get_token import admin_id, user_id
from test_data.reward.rank_data.data import new_rank
from test_data.reward.reward_data.data import new_reward_no_goal, new_reward, \
    new_reward_no_start_date, \
    new_reward_no_end_date, \
    new_reward_no_events, \
    invalid_reward_id
from test_data.reward.rank_data.data import new_rank_empty_name, \
    new_rank_empty_xp_points, \
    new_rank_empty_avatar

reward_create_api = Api("reward/create")


@allure.step("Validate user is able to create reward successfully")
def test_create_reward_valid():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201


@allure.step("Validate user is not able to create reward without goalname")
def test_create_reward_no_goal():
    result = reward_create_api.post_request(new_reward_no_goal, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without start date")
def test_create_reward_no_start_date():
    result = reward_create_api.post_request(new_reward_no_start_date, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without end date")
def test_create_reward_no_end_date():
    result = reward_create_api.post_request(new_reward_no_end_date, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward without events")
def test_create_reward_no_events():
    result = reward_create_api.post_request(new_reward_no_events, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create reward with get request")
def test_create_reward_get():
    result = reward_create_api.get_request(new_reward, headers=admin_headers_with_token)
    message = result['response']['message']
    assert message is "Internal server error"


@allure.step("Validate user is not able to create reward with put request")
def test_create_reward_put():
    result = reward_create_api.put_request(new_reward, headers=admin_headers_with_token)
    message = result['response']['message']
    assert message == "Internal server error"


@allure.step("Validate user is able to retrieve a reward by id")
def test_get_reward_by_id():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    reward_id = result['response']['data']['_id']
    get_reward = Api("reward/{}".format(reward_id))
    result = get_reward.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


@allure.step("Validate user is not able to retrieve a reward by invalid id")
def test_get_reward_by_invalid_id():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    reward_id = result['response']['data']['_id']
    get_reward = Api("reward/{}".format(reward_id))
    result = get_reward.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200
    get_reward = Api("reward/{}".format(invalid_reward_id))
    result = get_reward.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


@allure.step("Validate user is not able to retrieve a reward by POST request")
def test_get_reward_by_post():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    reward_id = result['response']['data']['_id']
    get_reward = Api("reward/{}".format(reward_id))
    result = get_reward.post_request(headers=admin_headers_with_token)
    retrieve_status_code = result['status_code']
    assert retrieve_status_code == 404


@allure.step("Validate user is able to delete a reward successfully with admin token")
def test_delete_reward_by_id():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    reward_id = result['response']['data']['_id']
    delete_reward = Api("reward/{}".format(reward_id))
    result = delete_reward.delete_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


@allure.step("Validate all rewards can be retrived successfully by admin")
def test_get_all_rewards():
    api = Api("reward/get-all")
    result = api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


@allure.step("Validate no rewards can be retrieved without token")
def test_get_all_rewards_with_user_token():
    api = Api("reward/get-all")
    result = api.get_request()
    status_code = result['status_code']
    assert status_code == 401


@allure.step("Validate rewards can be retrieved by user id")
def test_get_all_rewards_by_user_id():
    api = Api("reward/UserGoalsById/{}".format(admin_id))
    result = api.get_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


@allure.step("Validate rewards can not be retrieved by user id with POST request")
def test_get_all_rewards_by_user_id_with_post():
    api = Api("reward/UserGoalsById/{}".format(admin_id))
    result = api.post_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


@allure.step("Validate rewards can not be retrieved by user id with PUT request")
def test_get_all_rewards_by_user_id_with_put():
    api = Api("reward/UserGoalsById/{}".format(admin_id))
    result = api.put_request(headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 404


@allure.step("Validate user can edit a reward successfully")
def test_edit_reward_by_id():
    result = reward_create_api.post_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201
    reward_id = result['response']['data']['_id']
    edit_reward = Api("reward/{}".format(reward_id))
    result = edit_reward.put_request(new_reward, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 200


@allure.step("Validate user is able to create rank successfully")
def test_create_rank_valid():
    rank_api = Api("reward/rank")
    result = rank_api.post_request(new_rank, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 201


@allure.step("Validate user is not able to create rank with with empty name")
def test_create_rank_empty_name():
    rank_api = Api("reward/rank")
    result = rank_api.post_request(new_rank_empty_name, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create rank with with empty XPPOINTS")
def test_create_rank_empty_xp_points():
    rank_api = Api("reward/rank")
    result = rank_api.post_request(new_rank_empty_xp_points, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


@allure.step("Validate user is not able to create rank with with empty avatar")
def test_create_rank_empty_avatar():
    rank_api = Api("reward/rank")
    result = rank_api.post_request(new_rank_empty_avatar, headers=admin_headers_with_token)
    status_code = result['status_code']
    assert status_code == 400


