import cv2
import numpy as np
import time
#si no sucede nada poner este comando en la consola de la raspberry:  sudo /etc/init.d/motion stop
cap=cv2.VideoCapture(0)
objetos = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480)) #no es necesario ya que esta por predeterminado
    mask = objetos.apply(frame)
    
    cv2.imshow('testeo', frame)
    cv2.imshow('mascara', mask)
    #time.sleep(0.5)
    k = cv2.waitKey(30)
    if k == 27:
        print("parando programa")
        break
        

cap.release()
cv2.destroyAllWindows()
