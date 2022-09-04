import pyautogui

# 파일메뉴 클릭해보기

# 파일 메뉴 좌표
# pyautogui.sleep(3) # 3초대기
# print(pyautogui.position())

pyautogui.click(1567,12, duration = 1) # 해당 좌표를 마우스로 클릭
# 해당 동작은 아래 (버튼누르기, 버튼 떼기)를 합친 동작.
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# 좌표정보 안주면 현재 위치를 클릭.

# 더블 클릭
# pyautogui.doubleClick()
# pyautogui.click(clicks = 2)

# 드래그
# 빠른동작으로 수행이 안되면 duration을 설정해주자.
pyautogui.moveTo(100,100)
pyautogui.mouseDown() 
pyautogui.moveTo(200,300)
pyautogui.mouseUp()
pyautogui.drag(200, 200) # 현재 좌표 기준
pyautogui.dragTo(200, 200) # 절대 좌표 기준

pyautogui.rightClcik() # 오른쪽 클릭
pyautogui.middleClick() # 마우스 휠

# 스크롤
pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤 /아래:-300
