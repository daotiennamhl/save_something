# import
from selenium import webdriver
from time import sleep
from datetime import datetime
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import traceback


def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def writeToFile(filename, content, delimiter='\n'):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(content + delimiter)

def getTime():
    return str(datetime.now()).split('.')[0]

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
options.add_argument('headless')

# get shop
links = []
log_file = 'log_trace.txt'
with open('shop.md', 'r', encoding="utf-8") as f:
    links = f.read().split('\n')
    links = list(map(
        lambda s: f'https://shopee.vn/shop/{s.split()[0]}/search?page=0&sortBy=sales', links))

# declare & init
data = []
fields = ['shop_id', 'product_id', 'name', 'sold', 'sold_text', 'historical_sold',
          'historical_sold_text', 'price', 'price_text', 'time', 'rating']
file_name = 'data_trace_shop.csv'
browser = webdriver.Chrome(
    executable_path="./chromedriver.exe", chrome_options=options)
browser.maximize_window()

writeToFile(log_file, getTime())
# crawl
for link in links:
    browser.get(link)
    sleep(0.5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(0.5)
    waitElement(
        '//*[@class="shop-search-result-view__item col-xs-2-4"]', browser, 5)
    products = browser.find_elements_by_xpath(
        '//*[@class="shop-search-result-view__item col-xs-2-4"]')
    shop_name = waitElement(
        '//*[@class="shopee-seller-portrait__name"]', browser, 5)

    for product in products:
        product_detail_link = product.find_element_by_tag_name('a').get_attribute('href')
        _, shop_id, product_id = product_detail_link.rsplit('.', 2)
        name = product.find_element_by_class_name('_10Wbs-').text
        sold_text = ''
        sold = ''
        historical_sold_text = product.find_element_by_class_name('_1uq9fs').text
        historical_sold = historical_sold_text.split('/')[0].rsplit(' ')[-1]
        price_text = product.find_element_by_class_name('kNGSLn').text 
        price = price_text.split(' - ')[0][1:].replace('.', '')
        rating = ''
        data.append({
            'product_id': product_id,
            'shop_id': shop_id,
            'time': getTime(),
            'name': name if len(name) < 50 else name[:50],
            'sold': sold,
            'sold_text': sold_text,
            'historical_sold': historical_sold,
            'historical_sold_text': historical_sold_text,
            'price': price,
            'price_text': price_text,
            'rating': rating
        })
    
    writeToFile(log_file, f'{shop_name.text} {str(len(products))}')
    sleep(1)
browser.close()

with open(file_name, 'a', newline='', encoding="utf-8") as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    # writer.writeheader()
    writer.writerows(data)

writeToFile(log_file, getTime() + "\n")
print("DONE !")