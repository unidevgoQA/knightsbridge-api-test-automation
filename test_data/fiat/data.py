from utils.read_date import read_datetime
from utils.read_update_counter import read_counter

today = read_datetime()
counter_reading = read_counter()


new_deposit = {
    "depositDate": "{}.180Z".format(today),
    "amount": 100,
    "depositRefNo": "testrefinfo{}".format(counter_reading),
    "receiptImage": "https://www.google.com/images/branding/""googlelogo/2x/googlelogo_color_272x92dp.png",
    "currency": "NGN",
    "paymentMethod": "Bank",
    "status": "Approved",
    "userId": "testuserid{}".format(counter_reading),
    "bankId": "demobankid{}".format(counter_reading),
    "adminBankId": "demoadminbankid{}".format(counter_reading),
    "accTitle": "Test Account Title {}".format(counter_reading),
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

status = "Pending"

fiat_id = '61bc16a34a4be9001c58c726'
