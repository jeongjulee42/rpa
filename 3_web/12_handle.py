# 운영체제가 식별하기 위한 키 값.
# 브라우저마다 다른 핸들값을 부여를 해서 관리.
from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
# 핸들값
curr_handle = browser.current_window_handle
print(curr_handle)  # 현재 윈도우 핸들 정보 / CDwindow-2678E064FAD93FDB76AC2A505D997A49

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()
# 새창이 뜨며 브라우저가 2개가 됨.

handles = browser.window_handles  # 모든 핸들 정보를 가져오기
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)  # 각핸들로 이동
    print(browser.title)  # 브라우저의 제목을 표시
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행


# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("돌아오기")
browser.switch_to.window(curr_handle)
print(browser.title)

# 브라우저 컨트롤이 가능한지 확인
time.sleep(5)
browser.get("https://www.daum.net/")


time.sleep(3)
browser.quit()
