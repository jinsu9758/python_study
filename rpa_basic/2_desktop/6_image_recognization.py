import pyautogui
# 사진을 불러와서 화면내에서 위치를 찾아주는거임. 개신기하네

#youtube = pyautogui.locateOnScreen("youtube.png")
#print(youtube)
#pyautogui.click(youtube)

#discord = pyautogui.locateOnScreen("discord.png")
#print(discord)
#pyautogui.moveTo(discord, duration=2)

#똑같이 생긴 것들이 2개 이상일떄
#pyautogui.locateAllOnScreen("checkbox.png")

#for i in pyautogui.locateAllOnScreen("checkbox.png"):
#    print(i)
#    pyautogui.click(i, duration=0.25)

#checkbox = pyautogui.locateOnScreen("checkbox.png") #처음 발견하는 1개
#pyautogui.click(checkbox)

# locateOnScreen 속도 개선

# 1. GrayScale -> 흑백으로 만들어서 찾는거 / 정확성이 떨어질 수 있음.
#discord = pyautogui.locateOnScreen("discord.png", grayscale=True)
#print(discord)
#pyautogui.moveTo(discord, duration=2)


#pyautogui.mouseInfo()

# 2. 범위를 지정한다.
#discord = pyautogui.locateOnScreen("discord.png", region=(357, 14, 518-357, 24))
#print(discord)
#pyautogui.moveTo(discord, duration=2)


# 3. 정확도 조정하기  pip install opencv-python
#good_btn = pyautogui.locateOnScreen("good.png", confidence=0.9) #90퍼 센트이상 이미지 일치
#pyautogui.moveTo(good_btn, duration=0.25)



#자동화 대상이 바로 보이지 않는 경우
# 1. 계속 기다리기
#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#if file_menu_notepad:
#    pyautogui.click(file_menu_notepad)
#else:
#    print("발견 실패")

#while file_menu_notepad is None:
#    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#    print("발견 실패")

#pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

#timeout = 10
#start = time.time() # 시작시간 설정
#file_menu_notepad = None
#while file_menu_notepad is None:
#    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png") #계속적으로 찾아주기
#    end = time.time() #종료시간 설정
#    if end - start > timeout:
#        print("시간 종료")
#        sys.exit()
#pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("Timeout {}s , Target not found {}".format(timeout, img_file))
        sys.exit()
        

my_click("file_menu_notepad.png", 10)
