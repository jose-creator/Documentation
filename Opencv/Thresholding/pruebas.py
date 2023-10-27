import cv2
import numpy as np

img = cv2.imread('python-logo-master-v3-TM-flattened.png')

px = img[100,100]
#print(px)
azul = img[100,100,0]
#print(azul)

print(img.shape)
"""
print(img.size)
print( img.dtype )
"""
c = img[30:150, 75:200]


cv2.imshow("no",img)
cv2.imshow("si",c)

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  