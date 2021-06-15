# #캡챠 때문에 막혀서 로그인이 안됨 ㄹㅇㅋㅋ
# import time
# import requests
# import pyperclip # 캡챠 방지용 -> 클립보드에 저장한 뒤 복붙할 예
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

# res = requests.get("https://naver.com", headers=headers)

# browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe")

# #1. 네이버로 이동
# browser.get("https://naver.com")

# #2. 로그인 버튼 클릭
# elem = browser.find_element_by_class_name("link_login")
# elem.click()


# #3. ID, PW 입력하기
# Id = browser.find_element_by_id("id")
# Id.click()
# pyperclip.copy("아이디 입력")
# Id.send_keys(Keys.CONTROL,'v')
# time.sleep(1)
# #Id = browser.find_element_by_id("id").send_keys("아이디 입력") 가능


# Pw = browser.find_element_by_id("pw")
# Pw.click()
# pyperclip.copy("비밀번호 입력")
# Pw.send_keys(Keys.CONTROL,'v')
# time.sleep(1)


# #4. 로그인 버튼 클릭하기
# login = browser.find_element_by_xpath("//*[@id='log.login']")
# login.click()
# #login = browser.find_element_by_id("log.login").click()
# #time.sleep(3)

# #5. id를 새로 입력
# #Id = browser.find_element_by_id("id").clear() #기존에 적었던 id 내용 없애는 거

#=============================================================================#

# 이게 되노?

import time
import random
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe")

time.sleep(random.uniform(1,3))

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

browser.get(url)

#input_js = ' \
#        document.getElementById("id").value = "{id}"; \
#        document.getElementById("pw").value = "{pw}"; \
#    '.format(id = "jinsu9758", pw = "wlstn123")

input_id = "document.getElementById('id').value = '{}'".format("아이디 입력")
input_pw = "document.getElementById('pw').value = '{}'".format("패스워드 입력")


time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
#browser.execute_script(input_js)
browser.execute_script(input_id)
browser.execute_script(input_pw)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()







