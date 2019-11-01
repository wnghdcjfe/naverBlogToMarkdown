from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import requests
from bs4 import BeautifulSoup
import time 
import re 
from operator import itemgetter 

url = "http://www.petronet.co.kr/v3/jsp/pet/prc/foreign/KDFQ0100_l.jsp"
def get_page_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='./chromedriver', 
        options=chrome_options)
    driver.get(url)
    finded = driver.find_element_by_class_name("outcome_table line_green").text
    driver.close()
    return finded 

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser') 

def find_idx(a, b):
    return a.index(b) 

ret = getPage(url)  

tr = ret.find_all("tr", class_="")
cnt = 0
namelist = ['Dubai', 'Brent', 'WTI', 'Oman']
n = len(tr)  
result = "["
for i in range(len(tr[n - 1].contents)): 
    content = tr[n - 1].contents[i] 
    if str(content).strip() == "" or i == 1: 
        continue
    ret = re.sub(r'<(.+?)>', "", str(content).strip())  
    result += ('{"name":"' + namelist[cnt] + '"')
    result += (',"value":' + ret + '}') 
    if cnt != 3:
        result += ','
    cnt += 1

result += "]"

f = open("./inbum.json", mode = 'w' , encoding='utf8')
f.write(result)
f.close() 