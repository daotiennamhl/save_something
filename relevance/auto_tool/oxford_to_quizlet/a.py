# import
from statistics import mode
from selenium import webdriver
from time import sleep
import csv
import traceback
from datetime import datetime, timedelta
import re
from model import Model
from utils import *

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('incognito')
options.add_argument('headless')

def getLink(word):
    return f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}'

browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
browser.maximize_window()

# const
text_file = 'text.txt'
result_file = 'result.md'
words = []

# clear file content
writeToFile(result_file, '', '', 'w')

with open(text_file, 'r', encoding="utf-8") as f:
    rows = f.read().split('\n')
    words = map(lambda r: r.split(' ')[0], rows)

for word in words:
    browser.get(getLink(word))
    waitElement('//h1[@class="headword"]', browser, 10)
    
    # word, prn, mean, *ex
    prnAm = browser.find_element_by_class_name('phons_n_am')
    prn = prnAm.find_element_by_class_name('phon').text
    mean = browser.find_element_by_class_name('def').text
    listEx = browser.find_element_by_class_name('examples')
    ex = listEx.find_elements_by_class_name('x')[:]
    ex = map(lambda e: e.text, ex)

    model = Model(word, prn, mean, *ex)
    writeToFile(result_file, model.toString(), '', 'a')
    sleep(0.1)

browser.close()