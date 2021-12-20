import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.read_date import read_date
from utils.read_update_counter import read_and_update_counter

report_folder_name = f"{read_date()}_{read_and_update_counter()}"
# running testCases
command = f"pytest -s --alluredir=report_allure/{report_folder_name} " \
          f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"
subprocess.run(command, shell=True)

# generating report
command = f"allure serve report_allure/{report_folder_name}"
subprocess.run(command, shell=True)