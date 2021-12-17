from datetime import datetime


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))
