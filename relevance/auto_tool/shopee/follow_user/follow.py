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
def writeToFile(filename, content, delimiter='\n'):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(content + delimiter)

# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('incognito')
# options.add_argument('headless')

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

# login
browser.get(login_link)
waitElement('//button[text()="Đăng nhập"]', browser, 5)
browser.find_element_by_xpath('//input[@name="loginKey"]').send_keys(username)
browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
sleep(1)
browser.find_element_by_xpath('//button[text()="Đăng nhập"]').click()
sleep(3)

for index, link in enumerate(links):
    res = ''
    browser.get(link)
    sleep(0.5)
    page = 1
    while(1):
        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'shopee-product-rating__author-name'))
            )
            users = browser.find_elements_by_class_name('shopee-product-rating__author-name')
            for u in users[:]:
                res += u.text + " "
            page += 1
            xpath_page_ele = f'//*[@class="shopee-button-no-outline"][text()={page}]'
            waitElement(xpath_page_ele, browser, 10).click()
            writeToFile('log.txt', str(page), ' ')
            sleep(1)
        except Exception as e:
            traceback.print_exc()
            writeToFile('log.txt', f'total page in link {index}: {page - 1}')
            break
    sleep(3)

    res = re.compile('\s+').split(res)
    writeToFile('log.txt', f'raw reviews = {len(res)}')

    res = list(set(res))
    writeToFile('log.txt', f'remove duplicates = {len(res)}')

    res = list(filter(lambda username: '*' not in username, res))
    writeToFile('log.txt', f'remove anonymous = {len(res)}')

    list_followed_user = []
    with open('followed.txt', 'r', encoding="utf-8") as f:
        list_followed_user += f.read().split('\n')
    with open('need_unfollow.txt', 'r', encoding="utf-8") as f:
        list_followed_user += f.read().split('\n')
    
    res = list(set(res) - set(list_followed_user))
    writeToFile('log.txt', f'remove followed user = {len(res)}')

    for index, username in enumerate(res):
        browser.get(f'https://shopee.vn/{username}')
        try:
            time_online = waitElement('//div[@class="section-seller-overview-horizontal__active-time"]', browser, 3)
            if ("giờ" in time_online.text) or ("phút" in time_online.text):
                try:
                    waitElement('//button[text()="theo dõi"]', browser, 2).click()
                    cnt += 1
                    writeToFile('log.txt', f'+{index} +{cnt}. {username} {time_online.text}')
                    writeToFile('need_unfollow.txt', username)
                except: 
                    writeToFile('log.txt', f'Đã follow rồi {username}')
                    writeToFile('followed.txt', username)
            else:
                writeToFile('log.txt', f'Offline quá lâu {username}')
                writeToFile('followed.txt', username)
        except:
            writeToFile('log.txt', f'Đang tạm nghỉ bán {username}')
            writeToFile('followed.txt', username)
        sleep(0.5)

browser.close()