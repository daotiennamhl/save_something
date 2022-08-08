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
log_file = 'log.txt'
words = []

# clear file content
writeToFile(result_file, '', '', 'w')
writeToFile(log_file, '', '', 'w')

with open(text_file, 'r', encoding="utf-8") as f:
    rows = f.read().split('\n')

for i, row in enumerate(rows):
    if (len(row.split(' ', 1)) >= 2):
        word, de = row.split(' ', 1)
    else: word = row
    browser.get(getLink(word))
    try: 
        waitElement('//h1[@class="headword"]', browser, 5)
        
        # word, prn, mean, *ex
        prnAm = browser.find_element_by_class_name('phons_n_am')
        prn = prnAm.find_element_by_class_name('phon').text
        mean = browser.find_element_by_class_name('def').text
        listEx = browser.find_element_by_class_name('examples')
        ex = listEx.find_elements_by_class_name('x')[:]
        ex = list(map(lambda e: e.text, ex))

        if (len(ex) < 3): 
            ex.append('')
            ex.append('')
        if (prn in de): prn = ''

        model = Model(i, word, de, prn, mean, *ex)
        writeToFile(result_file, model.toString(), '', 'a')
        print(i)
        sleep(0.1)
    except Exception as e:
        print('errr = ')
        writeToFile(log_file, f'{i}. {word}\n{traceback.format_exc()}' )

browser.close()