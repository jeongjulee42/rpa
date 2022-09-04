# 프레임 전환
# <html>
#     <body>
#         <iframe>
#             <html>
#                 <body>

#                 </body>
#             </html>
#         </iframe>
#         <iframe>
#             <html>
#                 <body>

#                 </body>
#             </html>
#         </iframe>
#         <iframe>
#             <html>
#                 <body>

#                 </body>
#             </html>
#         </iframe>
#     </body>
# </html>
# 과 같이 사용. xpath 사용시 iframe에 들어가서 작업해야한다.
# w3school radio 사용
from selenium import webdriver
import time
browser = webdriver.Chrome('/Users/jeongju/Downloads/chromedriver')

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")
# elem = browser.find_element_by_xpath('//*[@id="male"]') 이렇게 하면 찾을수 없는 element가 된다.
browser.switch_to.frame('iframeResult')  # 프레임 전환.
elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

browser.switch_to.default_content()  # 상위로 빠져 나오기.


time.sleep(10)


browser.quit()
