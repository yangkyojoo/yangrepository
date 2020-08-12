# 셀레니움 연습하기
from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 네이버 지도 접속하기
driver.get("https://finance.daum.net/quotes/A045300")


for n in range(1, 20):
    # 지연시간주기
    time.sleep(1)
    stores = driver.find_elements_by_css_selector("span.numB")
    how = stores[0].find_element_by_css_selector("strong").text
    print(how)
