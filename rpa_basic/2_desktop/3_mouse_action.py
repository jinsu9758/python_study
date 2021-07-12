import pyautogui
#print(pyautogui.position())

#pyautogui.click(729, 311, duration=1) #1초동안 해당 좌표에 마우스 클릭

#보통이거는 드래그 할때 응용하는 거임.
#pyautogui.mouseDown() #누른거
#pyautogui.mouseUp() #뗀거


#더블 클릭
#pyautogui.doubleClick()
#pyautogui.click(clicks=500) #엄청 짧은시간에 클릭함.

#드래그1
#pyautogui.move(100, 100)
#pyautogui.mouseDown()
#pyautogui.move(300, 300)
#pyautogui.mouseUp()

pyautogui.sleep(3) #3초 대기
#pyautogui.rightClick() #마우스 오른쪽
#pyautogui.middleClick()

#print(pyautogui.position())

#드래그2
#pyautogui.moveTo(923, 192)
#pyautogui.drag(100, 0, duration=0.25) #너무 빠른 동작으로 drag가 수행이 안될때는 시간 주기
#pyautogui.dragTo(1514, 349, duration=0.25)

#스크롤 하기
pyautogui.scroll(300) #위 방향으로 300 이동, -300이면 아래 방향임
