from cgitb import reset
import pyautogui
# pyautogui.countdown(3) # 밑에있는 문장에 들어가기 전에 3초동안 카운트

# 사용자의 개입이 필요한 경우
# pyautogui.alert("자동화 수행에 실패", "경고") # 확인 버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행?","확인") # 확인, 취소버튼
# print(result)
# result = pyautogui.prompt("파일명은 뭘로할래?","입력") # 사용자 입력 받기
# print(result)

result = pyautogui.password("암호 입력","password") # 비밀번호 입력