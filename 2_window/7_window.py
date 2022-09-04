# 윈도우 관리하기
# 맥북은 지원이 안됨.
# 프로그램이 어느 위치에 있는지 받아오기.
import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 정보 가져오기 
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보

# pyautogui.click(fw.left + 40, fw.top + 20)

# 모든 윈도우 가져오기
# for w in pyautogui.getAllWindows():
#     print(w)

# 특정 윈도우
w= pyautogui.getWindowsWithTitle("스티커")[0]
if w.isActive == False: # 현재 활성화x이면
    w.activate() # 활성화, 맨앞으로 화면 가져오기

if w.isMaximized == False:  #현재 최대화가 되지 않았다면, 최소화는 minimized
    w.maximize() # 최대화

w.restore() # 원상복구

w.close() #윈도우 닫기
