from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')
browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[118]').click()
browser.find_element_by_xpath('//*[@id="fname"]').send_keys('나도')
browser.find_element_by_xpath('//*[@id="lname"]').send_keys('코딩')
browser.find_element_by_xpath(
    '//*[@id="country"]/option[text()="Canada"]').click()
browser.find_element_by_xpath(
    '//*[@id="main"]/div[3]/textarea').send_keys('퀴즈 완료하였습니다.')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
time.sleep(5)

browser.quit()
