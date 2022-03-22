import allure
from test_data.headers import admin_headers_with_token
from test_data.media.data import file
import requests


@allure.step("Verify that media upload is successful")
def test_media_upload():
    result = requests.post(url='https://api-qa.knights.app/media',
                           data=file,
                           headers=admin_headers_with_token.update({'Accept': '*/*',
                                                                    'Content-Type': 'multipart/form-data'}))
    status_code = result.status_code
    assert status_code == 201
