from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)


#특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 스크롤 방법
# 방법 1. ActionChain
#actions = ActionChains(browser)
#actions.move_to_element(elem).perform()


# 방법 2. : element가 위치하고 있는 좌표 정보를 주는거
#xy = elem.location_once_scrolled_into_view
#print(type(xy)) #dict형식
#print(xy)

time.sleep(5)

browser.quit()

