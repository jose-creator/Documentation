import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pilares.png')

blur = cv.bilateralFilter(img,9,75,75)

cv.imshow("si",img)
cv.imshow("a",blur)
if cv.waitKey(0) & 0xff == 27:  
    cv.destroyAllWindows()  
"""
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
"""
