import cv2 as cv
import numpy as np

img = np.zeros((599,599,3), dtype="uint8")
cv.rectangle(img,(0,0),(img.shape[0]//2,img.shape[1]//2),(95,104,255), thickness=cv.FILLED)
cv.rectangle(img,(img.shape[1]//2,0),(img.shape[1],img.shape[0]//2),(255,65,107),thickness=cv.FILLED)
cv.rectangle(img,(0,img.shape[1]//2),(img.shape[0]//2,img.shape[1]),(255,65,107),cv.FILLED)
cv.rectangle(img,(img.shape[1]//2,img.shape[1]//2),(img.shape[1],img.shape[0]),(95,104,255),cv.FILLED)
cv.line(img,(0,img.shape[1]//2),(img.shape[0],img.shape[1]//2),(0,0,0), thickness=18)
cv.line(img,(img.shape[0]//2,0),(img.shape[0]//2,img.shape[1]),(0,0,0), thickness=18)
cv.line(img,(0,img.shape[1]//2),(img.shape[0],img.shape[1]//2),(255,255,255), thickness=6)
cv.line(img,(img.shape[0]//2,0),(img.shape[0]//2,img.shape[1]),(255,255,255), thickness=6)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),60,(255,255,255),thickness=cv.FILLED)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),63,(0,0,0),thickness=6)

img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("Panel", img)
cv.waitKey(0)