# 이미지 기반 자동화
# 이미지를 화면에서 찾아서 동작하는 방식.
# 잔체화면을 하나의 이미지로 보고 거기서 해당 이미지를 찾아 그 영역을 말해준다.
import pyautogui
# file menu
# file_menu = pyautogui.locateOnScreen("file_menu.png") # 파일명, 파일 메뉴의 이미지가 저장된 파일.
# print(file_menu)
# pyautogui.click(file_menu)
# 이미지 없거나 발견 못하면 None이 나온다.

# 똑같이 생긴게 2개 이상인 경우 locateAllOnScreen을 통해 for문을 통해 해결이 가능.
# locateOnScreen은 첫번째로 발견되는것에 한해 동작.

# 속도 향상
# 1.그레이스케일 - 컬러 이미지를 흑백으로 전환하여 비교. 30프로 개선된 속도
# 정확도 떨어질수도 있음
file_menu = pyautogui.locateOnScreen("file_menu.png",grayscale=True)
pyautogui.click(file_menu)
# 2.범위를 지정.
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=(x,y,width,height))
# 으로 좌표를 지정.
pyautogui.click(file_menu)
# 3. 정확도 조정
# 설치 pip install opencv-python
file_menu = pyautogui.locateOnScreen("file_menu.png", confidence = 0.8)
# 80% 의 정확도, 기본값은 0.99
pyautogui.click(file_menu)


# 이미지처리 - 대상 
# 자동화 대상이 바로 보여지지 않는 경우. 어떤 대상이 뜰때까지 대기
while file_menu is None:
    file_menu = pyautogui.locateOnScreen("file_menu.png")
    
pyautogui.click(file_menu)

# 하염없이 기다리지 말기. - timeout 사용
# 일정 시간동안 기다리기
import time
import sys

timeout = 5 # 5초대기
start = time.time() # 시작시간 설정
file_menu = None
while file_menu is None:
    file_menu = pyautogui.locateOnScreen("file_menu.png")
    end = time.time() # 종료시간 설정
    if end - start > timeout: # 지정시간 초과하면
        sys.exit() # 프로그램 종료

pyautogui.click(file_menu)

# 함수로 사용하면 편하다.
def find_target(img_file, timeout= 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("timeout")
        sys.exit()


