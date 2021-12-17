from utils.read_update_counter import read_counter
from utils.email_reader import get_otp_from_email

username = 'test_user{}'.format(read_counter())
email = '{}@test.com'.format(username)

valid_user_data = {
  "email": "ss.unidev@gmail.com",
  "password": "5946644Ss@"
}

valid_email_password = {
  "email": "ss.unidev@gmail.com",
  "password": "5946644Ss@"
}


invalid_user_data = {
  "email": "ss.nasa@gmail.com",
  "password": "12345678"
}

empty_email_data = {
  "username": "",
  "password": "12345678"
}

empty_password_data = {
  "username": "ss.unidev",
  "password": ""
}

user_data_pass_length_less_than_6 = {
  "username": "ss.unidev@gmail.com",
  "password": "12345"
}

user_signup_data = {
  "email": email,
  "password": "5946644Ss@"
}

user_signup_invalid_password = {
  "username": username,
  "email": email,
  "password": "12345"
}

user_signup_empty_username = {
  "username": "",
  "email": email,
  "password": "5946644Ss@"
}

user_signup_empty_email = {
  "username": username,
  "email": "",
  "password": "5946644Ss@"
}

user_signup_invalid_email = {
  "username": username,
  "email": "nasa.com",
  "password": "5946644Ss@"
}

current_user_name_valid_data = {
  "username": "ss.unidev",
}

current_user_name_invalid_data = {
  "username": "ss.nasa",
}

current_user_name_empty_data = {
  "username": "",
}

only_valid_email = {
  "email": "ss.unidev@gmail.com"
}

only_invalid_email = {
  "email": "ss.nasa@gmail.com"
}

# user_with_otp_data = {
#   "email": "ss.unidev@gmail.com",
#   "otp": get_otp_from_email()
# }