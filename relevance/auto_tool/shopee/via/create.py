# import
from selenium import webdriver
from time import sleep
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import traceback
import pyautogui

def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
def writeToFile(filename, content, delimiter='\n'):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(content + delimiter)

def enter_proxy_auth(proxy_username, proxy_password):
    sleep(1)
    pyautogui.typewrite(proxy_username)
    sleep(1)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
# options.add_argument('headless')
PROXY = '103.3.246.14:49391'
options.add_argument(f'--proxy-server={PROXY}')

# declare & init
config = dotenv_values(".env")
username = config["username"]
password = config["password"]
cnt = 0

# declare
links = [
    r'https://shopee.vn/buyer/75973267/rating',
]
login_link = r'https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F'
browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
browser.maximize_window()
cnt = 0

browser.get('https://google.com')
proxy_username = "user49391"
proxy_password = "ktTTfmBXCC"
enter_proxy_auth(proxy_username, proxy_password)

# login
browser.get('https://facebook.com')
