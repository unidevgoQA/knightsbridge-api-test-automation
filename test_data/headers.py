from .get_token import token

bearer_token = 'Bearer ' + str(token)
headers_with_token = {'Authorization': bearer_token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
headers = {'Content-Type': 'application/json'}
