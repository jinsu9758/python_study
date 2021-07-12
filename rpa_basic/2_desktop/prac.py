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
    pyautogui.hotkey("enter")
    Sleep()
    w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
    w.activate()
    w.maximize()
    Sleep()
    Find_input_Text("text.png")
    Write_contents(result)
    End_mspaint(w)

    
if __name__ == "__main__":
    main()
