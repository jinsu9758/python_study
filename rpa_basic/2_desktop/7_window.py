import pyautogui
import time
#fw = pyautogui.getActiveWindow() #현재 활성화된 창 idle
#print(fw.title) #창의 제목 정보
#print(fw.size) #창의 크기 정보(width, height)
#print(fw.left, fw.top, fw.right, fw.bottom) #창의 좌표 정보
#pyautogui.click(fw.left + 10, fw.top + 20)

#for w in pyautogui.getAllWindows(): #모든 윈도우 들고오기
#    print(w)


#for w in pyautogui.getWindowsWithTitle("제목 없음"):
#    print(w)

# 현재는 새 메모장 띄어놓은 상태
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False:
    w.activate() #활성화( 맨 앞으로 가져오기 )

if w.isMaximized == False: #현재 최대화가 되지 않았다면
    w.maximize() #최대화
    time.sleep(1)

w.restore() #화면 원복

w.close() #윈도우 닫기


