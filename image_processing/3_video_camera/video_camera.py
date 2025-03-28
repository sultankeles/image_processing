import cv2

# capture
cap = cv2.VideoCapture(0)   # 0: default camera / If you use external camera, you have to choose one of them with 0 or 1.

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

# video record
writer = cv2.VideoWriter("video_record.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))  # 4-character code used to compress frames

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q") : break

cap.release()
writer.release()
cv2.destroyAllWindows()