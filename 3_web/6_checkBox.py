# 다중선택 가능.
from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')

time.sleep(5)


if elem.is_selected() == False:
    print("선택함")
    elem.click()
else:
    print("선택 안함")

time.sleep(5)
browser.quit()
