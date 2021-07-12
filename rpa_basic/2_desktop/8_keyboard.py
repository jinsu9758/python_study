import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개 띄운 상태
w.activate()

#pyautogui.write("12345") #쓰기
#pyautogui.write("hihhihihihihihihi", interval=0.25) #한글자 마다 0.25초

#pyautogui -> 한글은 지원안함.

#pyautogui.write(["t", "e", "s", "t","left","left", "right","1","a","enter"], interval=0.25)
#t e s t 적고, 마우스 커서 왼쪽 오른쪽 1적고 a적고 엔터

#https://automatetheboringstuff.com/2e/chapter20/
#찾기 : keyboard attribute


# 특수 문자
# shift + 4 -> $
#pyautogui.keyDown("shift")
#pyautogui.press("4")
#pyautogui.keyUp("shift")


#조합키
#pyautogui.keyDown("ctrl")
#pyautogui.keyDown("a")
#pyautogui.keyUp("a")
#pyautogui.keyUp("ctrl")

#간편한 조합키
#pyautogui.hotkey("ctrl","a")


#한글 처리하기
#pip install pyperclip

import pyperclip
#pyperclip.copy("찌아아쓰") # 해당 글자를 클립보드에 저장
#pyautogui.hotkey("ctrl","v") #클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    
my_write("찌아아쓰")






















