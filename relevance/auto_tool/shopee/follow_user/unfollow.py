# import
from selenium import webdriver
from time import sleep
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import traceback
def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
def writeToFile(filename, content, delimiter='\n', mode='a'):
    with open(filename, mode, encoding="utf-8") as f:
        f.write(content + delimiter)

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
options.add_argument('headless')

# declare & init
config = dotenv_values(".env")
username = config["username"]
password = config["password"]
cnt = 0

# declare
login_link = r'https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F'
browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
browser.maximize_window()
cnt = 0

# login
browser.get(login_link)
waitElement('//button[text()="Đăng nhập"]', browser, 5)
browser.find_element_by_xpath('//input[@name="loginKey"]').send_keys(username)
browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
sleep(1)
browser.find_element_by_xpath('//button[text()="Đăng nhập"]').click()
sleep(3)

list_followed_user = []
while True:
    with open('need_unfollow.txt', 'r', encoding='utf-8') as f:
        followed_user = f.read()
        username, need_unfollow = followed_user.split('\n', 1)
    browser.get(f'https://shopee.vn/{username}')
    try:
        waitElement('//button[text()="Đang Theo"]', browser, 2).click()
        writeToFile('log.txt', f'Hủy theo dõi {username}')
        writeToFile('followed.txt', username)
    except:
        writeToFile('log.txt', f'Chưa theo dõi {username}')
    writeToFile('need_unfollow.txt', need_unfollow, '', 'w')
    sleep(0.5)