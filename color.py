import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('Color')

cv2.createTrackbar('R', 'Color', 0, 200, nothing)
cv2.createTrackbar('G', 'Color', 0, 200, nothing)
cv2.createTrackbar('B', 'Color', 0, 200, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.setTrackbarPos('R', 'Color', 100)
cv2.setTrackbarPos('G', 'Color', 100)
cv2.setTrackbarPos('B', 'Color', 100)

while(True):
    ret, frame = cap.read()
    if not ret: continue
    
    r = cv2.getTrackbarPos('R', 'Color') / 100
    g = cv2.getTrackbarPos('G', 'Color') / 100
    b = cv2.getTrackbarPos('B', 'Color') / 100
    frame = frame / 255
    
    frame[:,:,2] *= r
    frame[:,:,1] *= g
    frame[:,:,0] *= b

    

    cv2.imshow('Color', frame)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()