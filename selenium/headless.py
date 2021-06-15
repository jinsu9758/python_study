from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36")

browser = webdriver.Chrome(r"C:\Users\CKIRUser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\jin\chromedriver.exe", options=options) #options는 여기 붙여주면 됨.
#browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

browser.get(url)

detected_value = browser.find_element_by_id("detected_value")

print(detected_value.text)

browser.quit()
