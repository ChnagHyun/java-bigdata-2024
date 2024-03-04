# file: p54_captWeather.py
# desc: 네이버 날씨화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '강원', '대전', '대구', '부산']

for region in regions:

    #auto.mouseInfo() #437,185
    auto.moveTo(76,111, duration = 0.5)
    auto.leftClick()
    for _ in range(5) :
        auto.press('delete')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl','v')# 붙여넣기
    time.sleep(0.2)

    auto.press('\n')# 'enter'도 가능
    time.sleep(1.0)
    #34,233   705,881

    startX, startY = 34, 233
    endX, endY = 705, 881
    im=auto.screenshot(region=(startX,startY,endX-startX,endY-startY))
    im.save(f'./day08/{region}날씨.png')
    #auto.screenshot(f'./day08/{region}날씨.png',
                # region=(startX, startY, endX-startX, endY-startY))
    print('저장완료!')