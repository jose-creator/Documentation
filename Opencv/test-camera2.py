import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #frame=cv2.resize(frame,(640,480))
    if not ret:
        print("fallo en capturar el frame")
        break
    cv2.imshow('testeo', frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("parando programa")
        break

cap.release()
cv2.destroyAllWindows()
