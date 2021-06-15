#할인하고 있는 영화정보만 스크래핑 해오기
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36","Accept-Language":"ko-KR,ko"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")


movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

#with open("movie.html","w",encoding="utf-8") as f:
#    f.wrtie(soup.prettify()) #html 문서를 예쁘게 출력해줌

# soup 객체를 html로 저장하여 브라우저에서 열었더니 영어 버전이 나옴.
# 한글 페이지를 잘 받아와야 함 -> user-agent

#len(movie)가 10개밖에 안 뜨는 이유 : 동적페이지 -> 스크롤을 내릴때 마다 업데이트가 되어서 화면이 채워지는 원리
#동적 페이지의 크롤링을 위해서 쓰는 것이 바로 selenium이다.


#for movie in movies:
#    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
#    print(title) #10개만 나옴.


# < selenium을 이용하여 동적 페이지 컨트롤하기 (로딩 + 스크롤내리기 + 로딩 + 스크롤 내리기 형식) >
# selenium 생성
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe")
browser.get(url)

# 지정한 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,2080)") #바탕화면 > 마우스 우클릭 > 디스플레이설정에서 pc 해상도 확인가능

# 화면 가장 아래로 스크로 내리기 ( 현재 문서의 총 높이만큼 스크롤 내림 )
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    prev_height = curr_height
    
print("스크롤 완료")