# 특정 영역 스크롤.
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://www.w3schools.com/html/")

browser.maximize_window()

time.sleep(3)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# 2가지 방법
# 1. 액션체인 from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()  # 이 엘리먼트까지 이동하는 동작을 수행해줘

# 2. 좌표정보 이용
# xy = elem.location_once_scrolled_into_view  # 함수가 아닌 변수.
# print("type:", type(xy))  # dict
# print("value:", xy)  # 위치 정보.

# 보이지 않는다고 없는게 아님. 스크롤을 하지 않아도 엘리먼트를 찾아 클릭이 가능.

elem.click()

time.sleep(3)
browser.quit()
