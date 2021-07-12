'''
아래의 동작을 자동으로 수행하는 프로그램을 작성하시오

1. 그림판 실행 (단축키 : Win + r, 입력값 : mspaint) 및 최대화

2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
 - 입력 글자 : "참 잘했어요"

3. 그림판 종료
이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료 되도록 함.
'''

#나의 코드
import pyautogui
import pyperclip
import time

def input_text():
    result = pyautogui.prompt("그림판에 입력할 문장을 적으시오", "입력")
    return result

def Sleep():
    time.sleep(1)

def Find_input_Text(file):
    text_img = pyautogui.locateOnScreen(file)
    pyautogui.click(text_img, duration=0.25)
    pyautogui.click(284, 378, duration=0.25)

def Write_contents(result):
    pyperclip.copy(result)
    pyautogui.hotkey("ctrl", "v")

def End_mspaint(w):
    w.close()
    Sleep()
    pyautogui.keyDown("n")
    pyautogui.keyUp("n")

def main():
    result = input_text()
    pyautogui.hotkey("winleft", "r")
    pyautogui.write("mspaint")
    pyautogui.hotkey("enter") #pyautogui.press("enter")
    Sleep()
    w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
    w.activate()
    w.maximize()
    #다른 방법
    '''
    if w.isMaximized == False:
        w.maximize() #최대화
    '''   
    Sleep()
    Find_input_Text("text.png")
    Write_contents(result)
    End_mspaint(w)

    
if __name__ == "__main__":
    main()
