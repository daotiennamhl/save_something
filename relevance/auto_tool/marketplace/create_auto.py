# import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import dotenv_values
from const import DISTRICT
from model import list_post
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitElement(xpath, browser, second):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


# option
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('incognito')
# options.add_argument('headless')

# declare & init
config = dotenv_values(".env")
listuser = config["listuser"].split(' ')
listpass = config["listpass"].split(' ')
cnt = 0

for username, password in zip(listuser, listpass):
    # start
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    # login
    browser.get('https://www.facebook.com')
    waitElement('//button[@name="login"]', browser, 8)
    browser.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    browser.find_element_by_xpath('//button[@name="login"]').click()
    sleep(1)
    for i, district in enumerate(DISTRICT):
        cnt += 1
        post = list_post[cnt%3]
        id_image = i + len(DISTRICT) * 3
        print(username, id_image)
        post.set_img_path(id_image)
        post.location = district
        # go to create marketplace page
        browser.get('https://www.facebook.com/marketplace/create/item')
        sleep(1)

        # add image
        waitElement('//input[contains(@accept, "image/*")]', browser, 8).send_keys(post.img_path)
        sleep(1)

        # add title, price, category, status, description
        # title
        waitElement('//label[@aria-label="Tiêu đề"]//input', browser, 8).send_keys(post.title)
        # price
        waitElement('//label[@aria-label="Giá"]//input', browser, 8).send_keys(post.price)
        # category
        waitElement('//label[@aria-label="Hạng mục"]', browser, 8).click()
        waitElement('//span[text()="Vườn"]', browser, 8).click()
        # status
        waitElement('//label[@aria-label="Tình trạng"]', browser, 8).click(); sleep(2)
        waitElement('//div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/span', browser, 8).click()
        # description
        waitElement('//label[@aria-label="Mô tả"]//textarea', browser, 8).send_keys(post.description)
        # send location
        location_element = waitElement('//input[@aria-label="Nhập tỉnh/thành phố"]', browser, 8)
        location_element.send_keys(Keys.CONTROL, 'A')
        location_element.send_keys(Keys.DELETE)
        location_element.send_keys(post.location)
        location_element.send_keys(Keys.ENTER)
        location_element.click()
        sleep(1)
        # choose location
        # waitElement('//ul/li/div/div[1]', browser, 8).click()
        WebDriverWait(browser, 8).until(
            EC.presence_of_all_elements_located((By.XPATH, '//ul/li/div/div[1]'))
        )[cnt%5].click()
        sleep(1)
        # ẩn với bạn bè, quảng cáo sau khi đăng
        [button.click() for button in browser.find_elements_by_xpath('//input[@aria-label="Đã bật"]')]
        sleep(1)
        # đăng
        waitElement('//div[@aria-label="Tiếp"]', browser, 8).click()
        sleep(1)
        waitElement('//div[@aria-label="Đăng"]', browser, 8).click()
        sleep(2)

    browser.close()

print('success')
# end
