from utils.read_update_counter import read_counter
from utils.email_reader import get_otp_from_email

username = 'test_user{}'.format(read_counter())
email = '{}@test.com'.format(username)

user_data = {
    "email": "knbridgetest@gmail.com",
    "password": "5946644Ss@"
}

reset_user_data_only_email = {
    "email": "knbridgetest@gmail.com"
}

reset_user_data_only_username = {
    "username": "testgooeyreset"
}

user_data_username_password = {
    "username": "testgooeyreset",
    "password": "5946644Ss@"
}

reset_email_credentials = {
    "email": "knbridgetest@gmail.com",
    "password": "5946644S"
}
reset_email_with_code = {
    "email": "knbridgetest@gmail.com",
    "code": ""  # code will be replace runtime
}
reset_email_with_invalid_code = {
    "email": "knbridgetest@gmail.com",
    "code": "1234"
}

user_with_new_password = {
    "email": "testgooeyreset@gmail.com",
    "newPassword": "5846{}644Ss@".format(read_counter()),
}
