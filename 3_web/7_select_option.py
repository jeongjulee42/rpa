# html option
from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame('iframeResult')

# 엘리먼트 찾고 드롭다운 내부의 4번쨰 옵션을 선택하기
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# 텍스트값을 통해 선택하기
# 옵션중에서 택스트가 audi인항목을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트값이 부분일차하는 항목 선택
elem = browser.find_element_by_xpath(
    '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(3)
browser.quit()
