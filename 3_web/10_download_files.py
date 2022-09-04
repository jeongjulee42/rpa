
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 경로 설정
chrome_options = Options()
chrome_options.add_experimental_option(
    'prefs', {'download.dafault_directory': '/Users/jeongju/Desktop/coding_project/rpa_basic'})
browser = webdriver.Chrome(
    '/Users/jeongju/Downloads/chromedriver', options=chrome_options)

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(3)
browser.quit()
