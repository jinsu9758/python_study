# 네이버 웹툰 크롤링 하기
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #//객체로 만들어줌

# print(soup.title)
# print(soup.title.get_text())
#print(soup.a) #처음 발견되는 a element를 반환
#print(soup.a.attrs) # a element의 속성을 반환
#print(soup.a["href"]) # a element의 href의 속성 값 정보를 출력할 수 있다.

#print(soup.find("a", attrs={"class" : "Nbtn_upload"})) 
#class="Nbtn_upload" 인 a element를 찾아줘
#print(soup.find(attrs={"class" : "Nbtn_upload"})) 
#class="Nbtn_upload" 인 어떤 element를 찾아줘

#print(soup.find("li",attrs={"class" : "rank01"})) 
rank01 = soup.find("li",attrs={"class" : "rank01"})
# print(rank01.a.get_text()) -
# # print(rank01.next_sibling)
# rank02 = rank01.next_sibling.next_sibling
# print(rank02.a.get_text())
# rank03 = rank02.next_sibling.next_sibling
# print(rank03.a.get_text())
#rank02 = rank03.previous_sibling.previous_sibling

#print(rank01.parent)

# rank02 = rank01.find_next_sibling("li") #다음 항목을 찾는데 li인것만 찾는거임
# print(rank02.a.get_text())
# rank03 = rank02.find_next_sibling("li")
# print(rank03.a.get_text())
# rank02 = rank03.find_previous_sibling("li")
# print(rank02.a.get_text())

# print(rank01.find_next_siblings("li")) -

# webtoon = soup.find("a", text="연애혁명-353. 그대안의 블루") -
# print(webtoon)











