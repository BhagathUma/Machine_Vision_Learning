import cv2 as cv
import numpy as np
"""Image"""
# img = cv.imread(r"Images\face.jpg")
# cv.imshow("Image",img)

# img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# haar = cv.CascadeClassifier("haar.xml")

# faces = haar.detectMultiScale(img_gray,1.1,3)

# for(x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0))

# print("No of Faces : ",len(faces))

# cv.imshow("Image",img)
# cv.waitKey(0)


"""Video"""
# haar = cv.CascadeClassifier("haar.xml")

# video =cv.VideoCapture(r"Videos\face.mp4")

# while(True):
#     ret,frame =video.read()
#     if(not ret):
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     faces =haar.detectMultiScale(gray,1.1,3)

#     for(x,y,w,h) in faces:
#         cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#         cv.putText(frame, "Face Detected", (x,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
    
#     cv.imshow("Video", frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# video.release()
# cv.destroyAllWindows()