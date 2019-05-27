from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import requests
from bs4 import BeautifulSoup
import time 
import re

blogId = "jhc9639"
postNumber = "221492245737"
url = "https://blog.naver.com/PostView.nhn?blogId=" + blogId + "&logNo=" + postNumber + "&redirect=Dlog&widgetTypeCall=true&directAccess=false"

def get_page_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='./chromedriver', 
        options=chrome_options)
    driver.get(url)
    finded = driver.find_element_by_class_name("se-quotation-container").text
    driver.close()
    return finded 

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser') 

ret = getPage(url)
code = ret.find_all("div", class_='se-code-source')
result = "" 
for tag in code:
    result += "```"
    result += tag.text
    result += "```" 
    result += "\n" 
 
blockquote_tag = ret.find_all("blockquote")
for tag in blockquote_tag:  
    if bool(re.search('[가-힣]|[a-z]|[0-9]',tag.text)):
        result += "# " + tag.text.strip()
        result += "\n" 

p_tag = ret.find_all("div", class_="se-section-text")
for tag in p_tag:  
    if bool(re.search('[가-힣]|[a-z]|[0-9]',tag.text)):
        result += tag.text 
        result += "\n" 

print(result) 
f = open("./kundol.md", mode = 'w' , encoding='utf8')
f.write(result)
f.close() 