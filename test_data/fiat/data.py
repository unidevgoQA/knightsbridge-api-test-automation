from utils.read_date import read_datetime
from utils.read_update_counter import read_counter

today = read_datetime()
counter_reading = read_counter()


new_deposit = {
  "depositDate": "2021-12-21T05:24:24.830Z",
  "amount": 200,
  "depositRefNo": "stringf{}".format(counter_reading),
  "receiptImage": "string",
  "currency": "string",
  "paymentMethod": "string",
  "status": "string",
  "userId": "string",
  "bankId": "string",
  "adminBankId": "string",
  "accTitle": "string"
}

fiat_search = {
    "pageNumber": 1,
    "pageSize": 1,
    "search": 1,
    "userId": new_deposit["userId"],
}

update_fiat = {
    "exchangeRate": 6
}

status = "Confirmed"
confirmed_status = "Confirmed"

fiat_id = '61bc16a34a4be9001c58c726'

fiat_withdraw = {
  "amount": 5,
  "userId": "string",
  "paymentMethod": "string",
  "currency": "string",
  "expectedPaymentDate": "{}T05:10:28.696Z".format(today),
  "bankName": "string",
  "title": "string",
  "country": "string",
  "swiftCode": "string",
  "accountNumber": "string"
}

admin_deposit = {
  "amount": 0,
  "currency": "string",
  "paymentMethod": "string",
  "userId": "string",
  "depositedBy": "string",
  "exchangeRate": 0
}

user_id = "testuserid{}".format(counter_reading)