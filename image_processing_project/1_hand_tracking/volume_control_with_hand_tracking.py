import cv2
import time
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Min and max volume
vol_min, vol_max, _ = volume.GetVolumeRange()

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

# Min and max point for distance
MIN_DISTANCE = 30
MAX_DISTANCE = 200

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
            
            h, w, c = img.shape
            thumb_tip = None
            index_tip = None
            
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 4:  
                    thumb_tip = (cx, cy)
                    cv2.circle(img, (cx, cy), 9, (130, 0, 130), cv2.FILLED)
                
                if id == 8:
                    index_tip = (cx, cy)
                    cv2.circle(img, (cx, cy), 9, (130, 0, 130), cv2.FILLED)
            
            # If two points are detected, calculate the distance
            if thumb_tip and index_tip:
                x1, y1 = thumb_tip
                x2, y2 = index_tip
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                
                # Draw a line and write the distance on the screen
                cv2.line(img, thumb_tip, index_tip, (130, 0, 130), 3)
                cv2.putText(img, f'{int(distance)} px', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Normalize distance between 0-1
                distance = max(MIN_DISTANCE, min(distance, MAX_DISTANCE))
                volume_level = ((distance - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE)) * (vol_max - vol_min) + vol_min
                
                # Adjust volume
                volume.SetMasterVolumeLevel(volume_level, None)
    
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f"FPS: {int(fps)}", (10, 75),
                cv2.FONT_HERSHEY_PLAIN, 3, (130, 0, 130), 5)
    
    cv2.imshow("img", img)
    cv2.waitKey(1)
