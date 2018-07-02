import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('GausianFillter', cv2.WINDOW_NORMAL)

cv2.createTrackbar('Variance', 'GausianFillter', 0, 50, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    ret, frame = cap.read()
    if not ret: continue
    variance =  cv2.getTrackbarPos('Variance', 'GausianFillter')
    frame = cv2.GaussianBlur(frame, (25, 25), variance)

    cv2.imshow('GausianFillter', frame)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()