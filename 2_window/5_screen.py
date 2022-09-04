import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")
# 안되면 pip install pillow

# vsc 버튼 누를때 확인하고 눌러보기
# pyautogui.mouseInfo()
# 1531,17 49,164,240 #31A4F0
pixel = pyautogui.pixel(1531,17) # 주어진 좌표에 해당하는 픽셀값을 가져옴
print(pixel) # rgb값.

pyautogui.pixelMatchesColor(1531,17,(49,164,240))
pyautogui.pixelMatchesColor(1531,17,pixel)
# true, false로 나온다.

