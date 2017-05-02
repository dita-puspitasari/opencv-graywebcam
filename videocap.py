import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())

while(cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()
    # Convert to gray image
    gimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting gray image on video
    cv2.imshow('webcam capture', gimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()