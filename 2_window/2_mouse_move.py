# 마우스 자동화
import pyautogui

# 마우스 이동
# 절대좌표 기준
# pyautogui.moveTo(1200,800) # 지정한 위치로 마우스를 이동.

# 마우스 천천히 이동
# pyautogui.moveTo(1200, 800, duration=0.25) # 0.25초 동안 지정한 좌표로 이동

# 마우스 이동하는 동작 
# pyautogui.moveTo(100,100, duration=0.25)
# pyautogui.moveTo(200,200, duration=0.25)
# pyautogui.moveTo(300,300, duration=0.25)

# 상대좌표로 마우스 이동( 현재 커서가 있는 위치로부터 이동)
pyautogui.move(100,100,duration = 0.25)

# 현재 마우스 위치 정보
print(pyautogui.position())
p = pyautogui.position()
print(p[0],p[1])
print(p.x, p.y)