# import 
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('incognito')
# options.add_argument('headless')
# declare and init
key_search = ["củ tỏi khô", "củ hành khô"]
scroll_times = 3
result = set()

# start
for k in key_search:
    # enter google
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get('https://www.google.com/')
    sleep(1)
    # enter key
    input = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input.send_keys(k)
    sleep(1)
    input.send_keys(Keys.RETURN)
    sleep(2)
    # choose image tab
    browser.find_element_by_xpath('//a[text()="Hình ảnh"]').click()
    sleep(2)

    # scroll n times
    for _ in range(scroll_times): 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(1)
    # get image_links
    panel = browser.find_element_by_id('islrg')
    list_img_element = panel.find_elements_by_xpath('.//img[@data-ils="4"]')
    print(len(list_img_element))
    for img_element in list_img_element:
        try:
            img_element.click()
            full_image_element = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
            img_link = full_image_element.get_attribute('src')
            result.add(img_link)
            print(len(result), img_link)
        except: # scroll more 100 pixel to get current image element
            print('need scroll more')
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollTop + 50)")
        finally:
            sleep(1)
    sleep(1)
    browser.close()
    sleep(1)

result = list(result) # convert from set to list

# write to OS
# create folder img
if not os.path.exists('C:/Users/daotiennam/Desktop/img'): 
    os.makedirs('C:/Users/daotiennam/Desktop/img')

# save to created folder
print('start write image')
for index, img_link in enumerate(result):
    try:
        image_data = requests.get(img_link).content
        with open(f'C:/Users/daotiennam/Desktop/img/{index}.jpg', 'wb+') as f:
            f.write(image_data)
        sleep(0.3)
    except Exception as e:
        print("error img_link")
print('success!')