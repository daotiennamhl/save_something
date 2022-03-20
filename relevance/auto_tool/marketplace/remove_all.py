# import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import dotenv_values
from const import DISTRICT
from model import post
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

# opton
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('incognito')
# options.add_argument('headless')

# declare & init
config = dotenv_values(".env")
username = config["username"]
password = config["password"]

# start
browser = webdriver.Chrome(options=options)
browser.maximize_window()

# login
browser.get('https://www.facebook.com')
waitElement('//button[@name="login"]', browser, 8)
browser.find_element_by_xpath('//*[@id="email"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
browser.find_element_by_xpath('//button[@name="login"]').click()
sleep(2)
cnt = 0
while(True):
    try:
        # go to list post
        browser.get('https://www.facebook.com/marketplace/you/selling')
        sleep(2)
        # press Option button
        waitElement('//span/div[contains(@class, "jktsbyx5")]/div[2]/div/div[1]/div', browser, 8).click()
        sleep(2)
        # choose Remove post
        waitElement('//div[contains(@class, "oqcyycmt")]/div[@aria-label="Xóa"]', browser, 8).click()
        sleep(2)
        # confirm remove
        waitElement('//div[contains(@class, "rq0escxv")]/div[@aria-label="Xóa" and @tabindex="0"]', browser, 8).click()
        sleep(2)
        print('remove success', cnt)
    except Exception as e:
        print("error: ", e)
        sleep(2)
        cnt += 1
        if cnt > 3:
            break

browser.close()