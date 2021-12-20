from random import choice
from utils.read_date import read_date
from utils.read_update_counter import read_counter
from api.common_api import Api
from test_data.headers import admin_headers_with_token

counter_reading = read_counter()

api = Api('survey/get-all')
result = api.get_request(headers=admin_headers_with_token)
random_survey = choice(result['response']['data'])
random_survey_id = random_survey['_id']
random_question = choice(random_survey['questions'])
random_question_id = random_question['_id']

new_survey = {
    "surveyName": "Survey Name {}".format(counter_reading),
    "questions": [
        {
            "statement": "Do you like knightsBridge?",
            "questionType": "check_box",
            "options": [
                "yes"
            ]
        }
    ],
    "isEmailRequired": True,
    "startDate": read_date(),
    "endDate": "2025-12-10"
}

update_survey = {
    "status": "deactivate"
}

filL_survey = {
    "userId": "618e89411cd07261c66cae10",
    "answers": [
        {
            "statement": "You can improve this app by {}".format(counter_reading),
            "questionType": "check_box",
            "options": [
                "yes"
            ],
            "questionId": random_question_id
        }
    ]
}

