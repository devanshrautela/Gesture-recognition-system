'''
made by parth shah TOOL KIT
youtube.com/c/TOOLKIT_Parth
gmail: toolkit.parth@gmail.com

'''

import cv2
import time
import HandTrackingModule as htm
import pyautogui as p
import os
import numpy as np
from sys import exit
import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    info = await current_session.try_get_media_properties_async()
    info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
    return info_dict['title']


os.popen(r"C:\Users\devan\AppData\Local\Microsoft\WindowsApps\Spotify.exe")

wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

time.sleep(3)
p.press('playpause')
print("pause/play")

detector = htm.handDetector(detectionCon = 0.6)

right = False
left = False
a = 0

def do():
    global wCam, hCam, cap, detector, left, right ,a
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    lmList = lmList[0]
    a = a + 1
    if len(lmList) != 0:
        x1, y1 = lmList[20][1], lmList[20][2]
        cv2.circle(img, (x1,y1), 10, (255,0,255), cv2.FILLED)
        if x1>= 550:
            if right:
                print('prev song')
                current_media_info = asyncio.run(get_media_info())
                p.press('prevtrack')
                left = False
                right = False
                time.sleep(0.5)
                current_media_info2 = asyncio.run(get_media_info())
                if current_media_info2 == current_media_info:
                    p.press('prevtrack')
            else:
                left = True
                a = 0
        elif x1 <= 50:
            if left:
                print('next song')
                p.press('nexttrack')
                left = False
                right = False
            else:
                right = True
                a = 0
        else:
            if x1>= 275 and x1<=325 and y1 <= 25:
                p.press('playpause')
                left = False
                right = False
                time.sleep(0.5)
    if a == 20:
        left = False
        right = False
        a = 0
    cv2.imshow('img',img)
    key = cv2.waitKey(5) & 0xFF
    if ord('q') == key:
        cv2.destroyAllWindows()
        cap.release()
        exit()

while True:
    do()
                
                