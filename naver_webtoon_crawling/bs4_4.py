# 평점 구하기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("div", attrs={"class":"rating_type"})

# 1.
# sum=0
# cnt=0
# for cartoon in cartoons:
#     result = cartoon.strong.get_text()
#     cnt+=1
#     sum+=float(result)

# print(sum/cnt)

total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))