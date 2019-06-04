from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import requests
from bs4 import BeautifulSoup
import time 
import re 
from operator import itemgetter 

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

def find_idx(a, b):
    return a.index(b) 

ret = getPage(url) 
result_arr = []

title = ret.find("div", class_="se-title-text")
result_arr.append({"name" : "title", "content" : title.text.strip()}) 

code = ret.find_all("div", class_='se-code-source') 
for tag in code:
    result_arr.append({"name" : "code", "content" : tag.text}) 
 
blockquote_tag = ret.find_all("blockquote")
for tag in blockquote_tag:  
    if bool(re.search('[가-힣]|[a-z]|[0-9]',tag.text)):
        result_arr.append({"name" : "blockquote", "content" : tag.text.strip()})  

p_tag = ret.find_all("div", class_="se-section-text")
for tag in p_tag:  
    if bool(re.search('[가-힣]|[a-z]|[0-9]',tag.text)):
        print(tag.text)
        result_arr.append({"name" : "content", "content" : tag.text})    

for i in range(len(result_arr)): 
    idx = find_idx(ret.text, result_arr[i]['content'])  
    result_arr[i]['idx'] = idx;  
    
newlist = sorted(result_arr, key=itemgetter('idx')) 
result = "" 
for item in newlist: 
    if item['name'] == 'title':
        result += ("# " + item['content'] + " \n")
    elif item['name'] == 'code':
        result += ("```\n" + item['content'] + "\n```\n")
    elif item['name'] == 'blockquote':
        result += ("## " + item['content'] + " \n") 
    elif item['name'] == 'content':
        result += (item['content'] + "\n")
f = open("./kundol.md", mode = 'w' , encoding='utf8')
f.write(result)
f.close() 