import cv2 as cv
import numpy as np

img=np.zeros((600,600,3), dtype='uint8')


cv.rectangle(img, (0,0), (300,300), (100,150,95), thickness=cv.FILLED)
cv.rectangle(img, (300,0), (600,300), (255,0,255), thickness=cv.FILLED)
cv.rectangle(img, (0,300), (300,600), (255,0,255), thickness=cv.FILLED)
cv.rectangle(img, (300,300), (600,600), (100,150,95), thickness=cv.FILLED)

cv.line(img, (300,0), (300,600), (0,0,0), thickness=6)
cv.line(img, (0,300), (600,300), (0,0,0), thickness=6)


cv.circle(img, (300,300), 60, (255,255,255), thickness=cv.FILLED)
cv.circle(img, (300,300),63, (0,0,0), thickness=6)





cv.imshow("Panel",img)
cv.waitKey(0)