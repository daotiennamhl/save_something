# import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import sys

def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def writeToFile(text):
    with open('res.txt', 'a', encoding="utf-8") as f:
        f.writelines(text + '\n')

split = lambda str : str.split(', ')
# formatTime = lambda time: time.strftime("%m/%d/%Y %H:%M:%S")
formatTime = lambda time: time.strftime("%Y/%m/%d %H:%M:%S")

# opton
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('incognito')
# options.add_argument('headless')

if __name__ == '__main__':
    try:
        index = sys.argv[1]
    except: 
        index = 1

# declare & init
config = dotenv_values(".env")
username = config[f"username{index}"]
password = config[f"password{index}"]
lUId = split(config[f"lUId{index}"])
lUName = split(config[f"lUName{index}"])

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
res = {uid:[(0, formatTime(datetime.now()))] for uid in lUId}
dictUser = {id:name for id, name in zip(lUId, lUName)}

while(True):
    browser.get('http://daotao.hnue.edu.vn/')
    sleep(5)
    try:
        bodyElement = browser.find_element_by_tag_name('body')
        writeToFile(formatTime(datetime.now()) + " ------ " + bodyElement.text[:len("Đăng nhập")])
        if (bodyElement.text != "The service is unavailable."):
            for uid in lUId:
                browser.get(f'https://www.facebook.com/messages/t/{uid}')
                waitElement('//div[@aria-label="Gửi lượt thích"]', browser, 5).click()
                sleep(3)
    except Exception as e:
        print('error: ', e)
    
    sleep(20)