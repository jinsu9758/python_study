import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#Headless 하는 법
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

url = "https://play.google.com/store/movies/top"

browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe", options=options) #options는 여기 붙여주면 됨.

browser.get(url)

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    #아래로 스크롤 내리
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
print("scroll complete")

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})


# print(len(movies)) #10개 나옴 -> 태그가 다름

for movie in movies:

    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
        title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    else:
        #print(title,"할인되지 않은 영화 제외")
        continue

    #할인 된 가격
    sale_price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 = url + link

    print("제목 : {}".format(title))
    print("할인 전 금액 : {}".format(original_price))
    print("할인 후 금액 : {}".format(sale_price))
    print("링크 : {}".format(url+link))
    print("-"*10)
    
browser.quit()
