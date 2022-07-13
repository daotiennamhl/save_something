# import
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import os
import requests
from model import Post
import json

# declare
start_link = r'https://shopee.vn/'
search_keys = ['hoa trà my', 'cây cảnh và hạt giống']
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
sleep(1)
  
# 1. get page
browser.get(start_link)
sleep(2)
browser.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div').click()
sleep(2)

# 2. search
search_text = browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/form/input')
search_text.send_keys(search_keys[0])
sleep(1)
search_text.send_keys(Keys.RETURN)
sleep(2)

# 3. craw data

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
i = 0
while True:
    i += 1
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/5 * {});".format(str(i)))

    # Wait to load page
    sleep(random.randint(1,2))

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

crawled_data = []
nodes_data = browser.find_elements_by_class_name('shopee-search-item-result__item')
print(len(nodes_data))
for node_data in nodes_data[1:]:
  link = node_data.find_element_by_css_selector('a').get_attribute('href')
  crawled_data.append(json.dumps(Post(link, '', '', '', '').__dict__))
print(crawled_data)
with open('./data.json', 'w') as f: f.write(json.dumps(crawled_data))
# close
sleep(2)
browser.close()


