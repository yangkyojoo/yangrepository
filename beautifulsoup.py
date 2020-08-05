import requests
from bs4 import BeautifulSoup as bs

url = "https://www.naver.com/"
html_text = requests.get(url).text

soup_obj = bs(html_text, "html.parser")
print(soup_obj)