#인트라넷 자동 메일 보내는 코드 테스트 작업

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

key = {"keyword1":"나 찐따아니다", "keyword2":"나 찐따맞다", "keyword3":"나 찐따맞냐?", "keyword4":"가슴이 웅장해진다"}
# 반별 이메일의 정보가 들어갈 자리

def create_browser(url):
    try:        #브라우저 여는 과정
        browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe")
        browser.get(url)
        return browser

    except:
        return -1
        
def login(browser, ID, PW):
    try:
        id_input = "document.getElementById('id').value = '{}'".format(ID)  #홈페이지 로그인 과정 넣을꺼
        pw_input = "document.getElementById('pw').value = '{}'".format(PW)
        time.sleep(random.uniform(1,3))
        browser.execute_script(id_input)
        browser.execute_script(pw_input)
        time.sleep(random.uniform(1,3))
        browser.find_element_by_id("log.login").click()

    except:
        return -1
        

class CLASS:    #반별로 클래스 만들꺼 
    def __init__(self, elem):
        self.elem = elem
        #print("클래스 생성 완료")
    def Send_Key(self, browser, key):     #이메일 보내는 기능넣을꺼 + 주간 or 야간 추가
        #self.elem = browser.find_element_by_id("query")
        self.elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,"query")))
        self.elem.send_keys(key)
        self.elem.send_keys(Keys.ENTER)



url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

ID = input('id 입력 : ')
PW = input('pw 입력 : ')
cl = int(input('몇반이십니까??? : '))

browser = create_browser(url)

login(browser, ID, PW)
elem=''
if cl == 1:
    print("1반입니다")
    class_1 = CLASS(elem)
    class_1.Send_Key(browser, key['keyword1'])  #이메일 보내기
    
elif cl == 2:
    print("2반입니다")
    class_2 = CLASS(elem)
    class_2.Send_Key(browser, key['keyword2'])

elif cl == 3:
    print("3반입니다")
    class_3 = CLASS(elem)
    class_3.Send_Key(browser, key['keyword3'])

elif cl == 4:
    print("4반입니다")
    class_4 = CLASS(elem)
    class_4.Send_Key(browser, key['keyword4'])
    


