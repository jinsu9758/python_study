import pyautogui
#스크린샷 찍기
#img = pyautogui.screenshot()
#img.save("screenshot.png") #파일로 저장

#pyautogui.mouseInfo()
#1168,913 2,133,224 #0285E0

pixel = pyautogui.pixel(1168, 913)
print(pixel)

# 해당 좌표에 있는 픽셀이 해당 rgb 값과 같은지 확인
print(pyautogui.pixelMatchesColor(1168, 913, (2,133,224)))
print(pyautogui.pixelMatchesColor(1168, 913, pixel))

