import pyautogui
#pyautogui.FAILSAFE = False # 멈추려고 해도 멈출수 없어!
#pyautogui.mouseInfo()

pyatuogui.PAUSE = 1 #모든 동작에 1초씩 sleep 적용

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)
