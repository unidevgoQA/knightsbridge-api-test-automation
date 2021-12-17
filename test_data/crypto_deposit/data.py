from utils.read_date import read_date
from utils.read_update_counter import read_counter

counter_reading = read_counter()

new_crypto_deposit = {
  "depositDate": "{}".format(read_date),
  "qty": 1,
  "depositRefNo": "refteest{}".format(counter_reading),
  "depositImage": "https://docrdsfx76ssb.cloudfront.net/static/1639060534/pages/wp-content/uploads/2020/05/illo"
                  "-mobile-810x480-1.jpg",
  "status": "Confirmed",
  "userId": "testuseerid{}".format(counter_reading),
  "walletId": "testwaelletid{}".format(counter_reading),
}

status = 'Confirmed'
deposit_id = "61bc737488929d001ddfc8ba"
