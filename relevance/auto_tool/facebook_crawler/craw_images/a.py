from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import os
import requests

### function define
def get_links_from_page(browser):
  urls = []
  node_urls = browser.find_elements_by_xpath("//a[starts-with(@href, '/marketplace/item')]")
  for node in node_urls:
    urls.append(node.get_attribute('href'))
  return urls

def scroll_page(browser):
  for i in range(0):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(random.randint(2, 3))

def open_new_tab_with_URL(browser):
  browser.execute_script('window.open("{}");'.format(url))
  browser.switch_to.window(browser.window_handles[1])
  sleep(1)

def get_img_links_by_xpath(xpath, browser):
  node_imgs = browser.find_elements_by_xpath(xpath)
  img_links = []
  for node_img in node_imgs[1:]:
    img_links.append(node_img.get_attribute('src'))
  return img_links

def save_img_to_local(post_id, img_links, district):
  folder_name = r"C:\Users\daoti\Desktop\img\{}".format(district)
  if not os.path.exists(folder_name): os.mkdir(folder_name)
  for index, img_link in enumerate(img_links):
    img_data = requests.get(img_links[index]).content
    with open('{}/{}...{}.jpg'.format(folder_name, post_id, index), 'wb+') as f:
      f.write(img_data)

def close_browser(browser, browser_index):
  browser.switch_to.window(browser.window_handles[browser_index])
  browser.close()

### main

start_links = [r"https://www.facebook.com/marketplace/110512632303092/search/?query=c%E1%BB%A7%20lan%20hu%E1%BB%87"]
districts = ["Quảng Ninh", "An Giang", "Đồng Tháp", "Quảng Nam", "Lâm Đồng", "Quảng Bình"]

for start_link in start_links:
  for district in districts:

    if not os.path.exists(r'C:\Users\daoti\Desktop\img\{}'.format(district)): os.mkdir(r'C:\Users\daoti\Desktop\img\{}'.format(district))

    # 1. declare & open browser
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    sleep(1)
    browser.get(start_link)
    sleep(2)
    print('end 1')

    location_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]")
    location_button.click()
    sleep(2)
    input_location = browser.find_element_by_xpath('//input[@aria-label="Nhập tỉnh/thành phố"]')
    input_location.send_keys(Keys.CONTROL + "a")
    input_location.send_keys(Keys.DELETE)
    input_location.send_keys(district)
    sleep(2)
    choose_suggest = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/ul/li[1]/div/div[1]')
    choose_suggest.click()
    sleep(2)
    apply_location = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div')
    apply_location.click()
    sleep(2)

    # 2. find list URL
    # a. scroll page
    scroll_page(browser)
    sleep(2)
    print('end 2 a')
    # b. get list urls
    urls = get_links_from_page(browser)
    sleep(1)
    # 3. new page
    for i in range(len(urls)):

      url = urls[i]
      post_id = url.strip("https://www.facebook.com/marketplace/item/").split("/")[0]
      # 3.a open new Tab with URLs
      open_new_tab_with_URL(browser)

      # 3.b get all imgs link
      xpath = '//img[@class="k4urcfbm bixrwtb6 datstx6m"][starts-with(@src, "https://scontent")]'
      img_links = get_img_links_by_xpath(xpath, browser)

      # 3.c close second window
      sleep(2)
      close_browser(browser, 1)
      browser.switch_to.window(browser.window_handles[0])

      # 3.d save img to local
      save_img_to_local(post_id, img_links, district)

      print('end 2 b', i)
      sleep(random.randint(2,4))

    # 6. close all browser
    close_browser(browser, 0)