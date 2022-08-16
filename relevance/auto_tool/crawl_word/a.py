# import
from selenium import webdriver
from time import sleep
import csv
import traceback
from utils import *
from datetime import datetime, timedelta
import re

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
# options.add_argument('headless')

browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
browser.maximize_window()

# const
result_file = 'result.md'
total_page = 11
link = r'https://www.trumtuvung.com/bo-tu-vung-danh-cho-dan-van-phong/page-'

for i in range(total_page):
    browser.get(f'{link}{i + 1}')
    waitElement('//h4[@class="media-heading"]', browser, 10)
    for j in browser.find_elements_by_class_name('media-heading'):
        writeToFile(result_file, str(j.text).split('/')[0])
    sleep(1)

browser.close()