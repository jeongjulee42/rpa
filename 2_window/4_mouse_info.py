import pyautogui
# pyautogui.mouseInfo() #를 통해 정보를 쉽게 얻을수있다.(실행해서 사용)

# 중간에 실패할때 자동화 프로그램을 중지해야한다. 
# 마우스를 귀퉁이에 내가 옮겨 넣기 -> 이러면 세션이 종료된다.
for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)
# 해당 옵션을 끄고싶다.
# pyautogui.FAILSAFE = False # 귀퉁이에 넣어도 끝나지 않는다. 비추천

# 동작이 너무 빠르니 각 함수별로 몇초씩 대기시켜서 동작시키는 방법.
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용.
