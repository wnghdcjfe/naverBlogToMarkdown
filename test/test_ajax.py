from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import requests
from bs4 import BeautifulSoup
import time 
import re 
from operator import itemgetter 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url = "http://www.opinet.co.kr/user/dopsravsel/DopSrAvselSelect.do" 
url = "http://www.opinet.co.kr/user/main/mainView.do"
def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass
 
def get_page_selenium(url):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='./chromedriver_win32/chromedriver', 
        options=chrome_options)
    driver.get(url)
    try:

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'siOsMin')))
        element = WebDriverWait(driver, 10)
        print(1)
        print(element)
        finded = driver.find_element_by_class_name("tab_type01").text 
        print(finded)
    finally:
        driver.quit()
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # table = soup.find('table', 'tab_type01') 
    # driver.close()
    # return table 

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser') 

def find_idx(a, b):
    return a.index(b) 

ret = get_page_selenium(url) 
# print(ret) 