import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#특정파일에 다운로드 받은것을 넣기 위한 코드
chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory' : r'C:\jin\3_web'})

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')


browser.switch_to.frame('iframeResult') #프레임 전환


#download link 클릭 -> 원하는 폴더에 다운로드가 되지 않는다.
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()
time.sleep(5)
browser.quit()


