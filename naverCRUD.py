import requests
from bs4 import BeautifulSoup

f = open("navertv.csv", "w")
f.write("제목,채널명,재생 수,좋아요 수")
raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

# replace함수를 활용해서 "재생 수" 제거
    hit = hit.replace("재생 수", "")
    # 슬라이싱을 활용해서 "좋아요 수" 제거
    like = like[5:]
    
    f.write(title + "," + chn + "," + hit + "," + like + "\n")

f.close()    