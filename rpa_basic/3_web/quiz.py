'''
Quiz) Selenium을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오.
    Follow link(ctrl + click)
1. https://www.w3schools.com 접속 (URL은 구글에서 w3school검색)
2. 화면 중간 LEARN HTML 클릭
3. 상단 메뉴 중 HOW TO 클릭
4. 좌측 메뉴 중 Contact Form 메뉴 클릭
5. 입력란에 아래 값 입력
    First Name : 나도
    Last Name : 코딩
    Country : Canada
    Subject : 퀴즈 완료하였습니다.
    * 위의 값들은 변수로 미리 저장해두세요
    
6. 5초 대기 후 submit 버튼 클릭
7. 5초 대기 후 브라우저 종료
'''

#내가 짠거
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def Interval(browser, xpath):
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return elem

def Start_sel(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    return browser

def Learn_Html(browser):
    elem = Interval(browser, '//*[@id="main"]/div[1]/div/div[1]/a[1]')
    elem.click()

def How_To(browser):
    elem = Interval(browser, '//*[@id="topnav"]/div/div/a[10]')
    elem.click()

def Contact_Form(browser):
    xpath = '//*[@id="leftmenuinnerinner"]/a[116]'
    elem = browser.find_element_by_xpath(xpath)
    actions = ActionChains(browser)
    actions.move_to_element(elem).perform()
    elem.click()

def Input_Content(browser, **kwargs):
    First_Name = Interval(browser, '//*[@id="fname"]')
    First_Name.send_keys(kwargs['First_n'])

    Last_Name = Interval(browser, '//*[@id="lname"]')
    Last_Name.send_keys(kwargs['Last_n'])

    Country = Interval(browser, '//*[@id="country"]/option[2]')
    #Country = browser.find_element_by_xpath('//*[@id="country"]/option[3]')
    Country = browser.find_element_by_xpath('//*[@id="country"]/option[text()="Canada"]')
    Country.click()
    
    Subject = Interval(browser, '//*[@id="main"]/div[3]/textarea')
    Subject.send_keys(kwargs['Subject'])
    #print(kwargs['First_n'])
    
def End(browser):
    time.sleep(5)
    Submit = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a')
    Submit.click()
    time.sleep(5)
    browser.quit()
    

if __name__ == "__main__":
    url = "https://www.w3schools.com/"

    #contents = {'First_n' : '나도', 'Last_n' : '코딩', 'Subject' : '퀴즈 완료하였습니다.'}
    
    browser = Start_sel(url)
    
    Learn_Html(browser)
    
    How_To(browser)
    
    Contact_Form(browser)

    Input_Content(browser, First_n="나도", Last_n="코딩", Subject="퀴즈 완료하였습니다.")

    End(browser)
    
