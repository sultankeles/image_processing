import cv2
import time

video_name = "MOT17-04-DPM.mp4"

# Video importing / Capture / Cap

cap = cv2.VideoCapture(video_name)

print("weight: ", cap.get(3))
print("height: ", cap.get(4))

if cap.isOpened() == False:
    print("Error")
    
# reading video
while True:
    ret, frame = cap.read() # frame: each image in the video / return(ret): whether the process was successful
        
    if ret == True:
        time.sleep(0.01)    # Used to slow down the video. If not used, the video will stream quickly.
        cv2.imshow("video", frame)
    
    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"):  # When we press the q key, the video will close.
        break
    
cap.release()   # stop capture
cv2.destroyAllWindows()