from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def waitElement(xpath, browser, second = 5):
    return WebDriverWait(browser, second).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def writeToFile(filename, content, delimiter='\n'):
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(content + delimiter)

def getTime():
    return str(datetime.now()).split('.')[0]

def convertTextToNumber(text):
    return int(re.sub(r'[^\d]', '', text))

def Buy10Give2(quantity):
    return quantity + int(quantity/10)
