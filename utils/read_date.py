from datetime import datetime


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# function to read current date and time
def read_datetime():
    return str(datetime.today().strftime('%Y-%m-%dT%H:%M:%S'))
