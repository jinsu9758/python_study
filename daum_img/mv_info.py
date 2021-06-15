# 다음 역대 관객 영화 순위 제목 평점 참여 개봉 누적 크롤링하기

import re
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

res = requests.get(url, headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

mv_name = soup.find_all("div", attrs={"class":"info_tit"}) # 영화 제목

rate = soup.find_all("em", attrs={"class":"rate"})  # 평점

rate_cnt = soup.find_all("a", attrs={"class":"link_count"}) # 평점 참여 수

mv_start = soup.find_all("dd", attrs={"class":"cont"})[0:60:2] # 개봉 일

mv_seen = soup.find_all("dd", attrs={"class":"cont"})[1:60:2] # 누적 관람객

#get_text()는 기본적으로 값이 일때 됨
# print(rate[0].get_text())  ->O
# print(rate.get_text()) -> X


for cnt in range(len(mv_name)):
    print("{}. {}".format(cnt+1, mv_name[cnt].get_text())) # 순위. 영화제목
    print("평점 : {}".format(rate[cnt].get_text()))
    print("평점 참여 수 : {}".format(rate_cnt[cnt].get_text())[:-2])
    print("개봉일 : {}".format(mv_start[cnt].get_text()))
    print("누적 관람객 : {}".format(mv_seen[cnt].get_text()))
    print("="*30)
    print()


