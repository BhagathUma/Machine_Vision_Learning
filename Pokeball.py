import cv2 as cv
import numpy as np

img = np.zeros((599,599,3), dtype="uint8")
cv.rectangle(img,(0,0),(img.shape[0],img.shape[1]//2),(255,0,0), thickness=cv.FILLED)
cv.rectangle(img,(0,img.shape[1]//2),(img.shape[0],img.shape[1]),(255,255,255), thickness=cv.FILLED)
cv.line(img,(0,img.shape[1]//2),(img.shape[0],img.shape[1]//2),(0,0,0), thickness=24)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),60,(255,255,255),thickness=cv.FILLED)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),66,(0,0,0),thickness=24)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),30,(0,0,0),thickness=2)
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),250,(0,0,0),thickness=24)

img_copy = img.copy()
for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    if(np.sqrt((i-img.shape[0]//2)**2 + (j-img.shape[1]//2)**2)>250):
      img_copy[i,j] = [0,0,0]
    else:
      img_copy[i,j]=img[i,j]

cv.putText(img_copy, "Gotta catch 'em all!", (120,55),color=(255,255,255),fontScale=1.2,fontFace=cv.FONT_HERSHEY_SIMPLEX,thickness=2)
pokeball=cv.cvtColor(img_copy,cv.COLOR_BGR2RGB)

cv.imshow("PokeBall",pokeball)
cv.waitKey(0)