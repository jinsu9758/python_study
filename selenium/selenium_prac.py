# 파이썬 코드파일 이름은 라이브러리 이름과 같으면 안된다

from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # 값(key) 집어넣을 때 필요한 라이브러리


browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe")
# 크롬 브라우저 열

browser.get("http://naver.com") # 홈페이지 창 열기

elem = browser.find_element_by_class_name("link_login")
# class가 link_login인 요소 받아오기

'''
elem.click()      # 클릭
browser.back()    # 이전 페이지 이동
browser.forward() # 다음 페이지 이
browser.refresh() # 새로고침

'''

elem = browser.find_element_by_id("query")
# id가 query인 요소 받아오기

# 값 집어넣기
elem.send_keys("나도 코딩")
elem.send_keys(Keys.ENTER) # 엔터

# 태그로 받아오기
elem = browser.find_elements_by_tag_name("a")
for e in elen:
    e.get_attribute("href")

#name으로 요소 받아오기
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")

#xpath로 요소 받아오기
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click() #클릭 동작

# 브라우저 닫기
browser.close() # -> 현재 탭만 닫는거
browser.quit() # -> 모든 탭 닫는거
