import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.read_date import read_date
from utils.read_update_counter import read_and_update_counter

report_folder_name = f"{read_date()}_{read_and_update_counter()}"
# running testCases
command = f"py.test -s --alluredir=report_allure/{report_folder_name} " \
          f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"
os.system(command)

# generating report
command = f"allure serve report_allure/{report_folder_name}"
os.system(command)
