import cv2
import numpy as np
#si no sucede nada poner este comando en la consola de la raspberry:  sudo /etc/init.d/motion stop
cap=cv2.VideoCapture(0)
"""
lower_range=np.array([150,142,7])
upper_range=np.array([179,255,255])
lower_range1=np.array([56,36,26])
upper_range1=np.array([88,255,255])

def red(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range,upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    a = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            a.append(x)
            x1 = int(x+x+w)//2
            y1 = int(y+y+w)//2
            cv2.circle(img,(x1,y1),4,(255,0,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    
    r=len(a)
    cv2.putText(frame,("Red: " + str(r)),(111,432),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    
    return int(r)
    

def green(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range1,upper_range1)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    b = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            b.append(x)
            x2 = int(x+x+w)//2
            y2 = int(y+y+w)//2
            cv2.circle(img,(x2,y2),4,(255,0,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    
    g = len(b)
    cv2.putText(frame,("Green: " + str(g)),(200,432),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
    
    return int(g)
    
""" 
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    #red(frame)
    #green(frame)
    #g2 = int(g1)
    #r2 = int(r1)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
"""
    if red(frame) > 0:
        print("a")
    elif green(frame) > 0:
        print("b")
"""
cap.release()
cv2.destroyAllWindows()
