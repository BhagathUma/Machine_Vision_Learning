import cv2 as cv
import numpy as np
"""reading images"""

# img = cv.imread("Images\cat1.jpg")
# cv.imshow("Cat", img)
# cv.waitKey(0)

"""reading video"""

# video = cv.VideoCapture("Videos/dog.mp4")

# while True:
#     is_True, frame = video.read()

#     if not is_True:
#         break

    
#     frame = cv.resize(frame,(500,500))
#     cv.imshow("Dog",frame)
#     if cv.waitKey(1) == ord('d'): 
#         break

# cv.destroyAllWindows()
# video.release()


"""Capturing Video"""

# video =cv.VideoCapture(0)


# while(True):
#     is_true,frame=video.read()

#     if not is_true:
#         break
#     cv.imshow("Video",frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# cv.destroyAllwindows()
# video.release()


"""Writing and drawing n  images"""

# blank_img = np.zeros((600,600,3), dtype='uint8')


# for i in range(600):
#     for j in range(600):
#         if(j<200):
#             blank_img[i,j] = (255,0,0)
#         elif(j>=200 and j<400):
#             blank_img[i,j] = (0,255,0)
#         else:
#             blank_img[i,j] = (0,0,255)


# cv.rectangle(blank_img, (25,25), (450,450), (100,150,95), thickness=20)
# cv.rectangle(blank_img,(25,25),(450,450),(100,150,95), thickness=cv.FILLED)

# cv.circle(blank_img, (250,250), 40, (100,150,95), thickness=cv.FILLED)

# cv.line(blank_img,(0,0),(300,300),(100,34,180), thickness=6)

# cv.putText(blank_img, "Hi:)", (300,300), color=(100,34,180), fontScale=2, fontFace=cv.FONT_HERSHEY_COMPLEX)


# cv.imshow("Blank_image",blank_img)
# cv.waitKey(0)


