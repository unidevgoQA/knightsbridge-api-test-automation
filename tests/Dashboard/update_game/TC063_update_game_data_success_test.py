import json
import allure
from api.common_api import Api
from test_data.headers import headers_with_token
from test_data.game_data.data import game_id_2

json_data = json.loads(open('../test_data/game_data/newData.json').read())
print(json_data)

# @allure.step("Update game data success test")
# def test_update_game_data_with_id():
#     url = "api/dashboard/games/id/{}".format(game_id_2)
#     games_api = Api(url)
#     response = games_api.put_request(json=, headers=headers_with_token)
#     assert response.status_code == 200
