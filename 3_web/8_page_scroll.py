# 동적페이지 스크롤.
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://shopping.naver.com/home/p/index.naver")

# 무선마우스 입력
elem = browser.find_element_by_xpath(
    '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER)

# 검색버튼 클릭
# browser.find_element_by_xpath(
#     '//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/button[2]').click()

# 스크롤

# 지정한 위치로 스크롤 내리기.
# 모니터 해상노 높이인 1080 위치로 스크롤 내리기( 즉 한페이지)
# browser.execute_script('window.scrollTo(0, 1080)')

# 화면 가장 아래로 스크롤 내리기.
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 맨 아래까지 로딩하기.
# 동적페이지에 대해 마지막까지 스크롤 반복 수행
interval = 1  # 1초에 한번씩 스크롤 내리기

# 현재 문서 높이 가져와서 저장.
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script(
        'window.scrollTo(0,document.body.scrollHeight)')

    # 직전 높이와 같으면(높이 변화가 없으면) 반복문 탈출. 스크롤 동작 완료
    if curr_height == prev_height:
        break

    prev_height = curr_height

time.sleep(3)
# 맨 위로 페이지 올리기
browser.execute_script('window.scrollTo(0,0)')

time.sleep(3)
browser.quit()
