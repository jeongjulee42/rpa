# 라디오 버튼 - 여러개중 택 1
# 클릭이 안되어있을때만 클릭하도록.
from selenium import webdriver
import time
browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('//*[@id="html"]')

# 체크 안되어있으면 선택하기.
if elem.is_selected() == False:  # 라디오 선택 x이면
    elem.click()

else:
    print("선택됨")

# browser.switch_to.default_content()  # 상위로 빠져 나오기.


time.sleep(5)

if elem.is_selected() == False:  # 라디오 선택 x이면
    elem.click()

else:
    print("선택됨")

browser.quit()
