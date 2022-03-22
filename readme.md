# KNIGHTSBRIDGE API TESTING

This project is a starting point for `KNIGHTSBRIDGE` API testing.

### API Routes:

Base URL : `https://api-dev.knights.app/` <br />
Sign up : `/api/auth/signup`<br />
Sign in : `/api/auth/signin`<br />
Get user: `/api/auth/get-user-by-username`<br />
verify: `/api/auth/verify-email`<br />
verify OTP: `/api/auth/verify-otp`<br />
Send OTP: `/api/auth/send-otp`<br />
Reset Password: `/api/auth/reset-password`<br />

### Sing Up

Route is tested for different combination of payload :

`with only email`,
`with only password`,
`without email & password`,
`with email & password`,
`with only email`,
`with only password`,
`with no email & password`,
`with email & no password`

Route is tested for different request methods:

`GET`, `POST`, `PUT` , `Delete`, `Options`

Response code, body, field & messages are asserted according to test scenarios:

`200`,`201`,`204` for successful request. Fields from response body asserted for successful request.

`400`,`404`  for bad or failed request. Error messages from response body asserted for failed or bad request.

N.B: Successfully created user credentials are stored in an Excel file.

### Sing In

Route is tested for different combination of payload :

`with only email`,
`with only password`,
`without email & password`

Route is tested for different request methods:

`GET`, `POST`, `PUT` , `Delete`, `Options`

Response code, body, field & messages are asserted according to test scenarios:

`200`,`201`,`204` for successful request. Fields from response body asserted for successful request.

`400`,`404`  for bad or failed request. Error messages from response body asserted for failed or bad request.

### Get User with username

Route is tested for different combination of payload :

`with Bearer token`,
`without Bearer token`

Route request method:

`PUT`

Response code, body, field & messages are asserted according to test scenarios:

`200` for successful request. Fields from response body asserted for successful request.

`400` for bad request. Error messages from response body asserted for bad request.

## Project Structure

`tests`: All testcases belongs here<br />
`test_data`: All data related to testcases belongs here<br />
`test_conf`: Project settings configuration & run commands are stored her<br />
`utils`: Utility functions are stored here.

## Installation

##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ Linux/Mac - run: pip3 install -r requirements.txt
    - Windows   - run: pip install -r requirements.txt

## Run Project


    $ Linux/Mac > run: python3 test_conf/runtest.py
    $ Windows   > run: python test_conf/runtest.py

## Run Project parallel


    $ > run: py.test -n auto

`auto` flag will determine the amount of threads automatically.
