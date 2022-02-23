from test_data.get_token import user_id


new_activity_log = {
  "userId": user_id,
  "eventName": "signup",
  "userEmail": "ehtsham@technowis.co",
  "description": "User X did n amount of deposit",
  "amount": 6,
  "status": "success"

}

new_activity_log_no_event_name = {
  "userEmail": "ehtsham@technowis.co",
  "description": "User X did n amount of deposit",
  "amount": 6,
  "status": "success"
}

new_activity_log_no_email = {
  "userId": user_id,
  "eventName": "signup",
  "description": "User X did n amount of deposit",
  "amount": 6,
  "status": "success"

}


new_activity_log_no_amount = {
  "userId": user_id,
  "eventName": "signup",
  "userEmail": "ehtsham@technowis.co",
  "description": "User X did n amount of deposit",
  "status": "success"

}

new_activity_log_no_status = {
  "userId": user_id,
  "eventName": "signup",
  "userEmail": "ehtsham@technowis.co",
  "description": "User X did n amount of deposit",
  "amount": 6,

}