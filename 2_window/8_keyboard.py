import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("nado coding", interval=1) # 천천히 적기
# 한글로 적으면 글자가 적히지 않는다. 영문과 숫자만 적용된다.

pyautogui.write(["t","e","s","t","left","right","left","l","a","enter"], interval=0.25)
# test 순서대로 적고 왼쪽 방향키, 오른쪽 방향키, 엔터키까지 실행.
# automate the boring stuff with python 검색, #20-1

# 특수문자
# shift + 4 -> $
pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# 조합키(hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")
# 전체선택 ctrl + a

# 간편한 조합키
# pyautogui.hotkey("ctrl","a")
# ctrl 누르고 a누르고 a떼고 ctrl 떼고

# 한글 처리
# pip install pyperclip
import pyperclip
# 어떤 문장을 클립보드에 집어넣기(복사한 내용을 임시로 가지고 있는 공간)
pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드에 저장
pyautogui.hotkey("ctrl","v")

# 함수로 설정해서 쓰자.

# win : ctrl + alt + del 누르면 화면전환-> 자동화 종료
# MAC : cmd + shift + option + q