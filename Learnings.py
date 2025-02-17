import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
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
# cv.destroyAllWindows()
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


"""Basic Functions"""

# img = cv.imread("Images/leaf.jpg")

##Color to gray
# img= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY IMAGE",img)

##blur
# img = cv.blur(img,(3,3),0)
# cv.imshow("Blurred image",img)

##edge detection

# img=cv.Canny(img, 135,175)
# cv.imshow("Edge detected image",img)

##resize
# img=cv.resize(img,(1200,1200))
# cv.imshow("Resized image",img)


"""Image transformation"""
# img = cv.imread("Images\cat2.jpg")

# #translation

# def translation(img,x,y):
#     trans_Matrix=np.float32([[1,0,x],[0,1,y]])

#     return cv.warpAffine(img,trans_Matrix,(img.shape[0],img.shape[1]))
# img = translation(img,10,10)

# #flip

# # 0 -> vertical flip
# # 1 -> horizontal flip
# # -1 -> both vertical and horizontal flip
# img=cv.flip(img,0)



# cv.imshow("Translated image",img)

# cv.waitKey(0)

"""Contour detection"""
# img=cv.imread(r"Images/cat1.jpg")
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # Canny=cv.Canny(gray,125,175)
# ret, thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)

# contours, highrar =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(len(contours))

# blank=np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype="uint8")
# cv.drawContours(blank,contours,-1,(255,0,0),2)

# blank=cv.resize(blank,(800,600))
# cv.imshow("thresh",blank)

# cv.waitKey(0)

"""Color Space"""

# img=cv.imread("Images\Colorful.jpg")
# cv.imshow("Colorful",img)
# #BGR2RGB
# rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("RGB",rgb)

# #BGR2HSV
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

# #BGR2LAB
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)

# #BGR2GRAY
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

# b,g,r =cv.split(img)
# cv.imshow("B",b)
# cv.imshow("G",g)
# cv.imshow("R",r)
# img_merged=cv.merge([b,g,r])
# cv.imshow("Merged",img_merged)

# cv.waitKey(0)


"""Smoothing Techniques"""
# img=cv.imread(r"Images\dog2.jpg")

# #average blur
# blur_img = cv.blur(img,(3,3))

# #Gaussian blur
# blur_img=cv.GaussianBlur(img, (3,3), 5) 

# #Median blur
# blur_img=cv.medianBlur(img, 3)

# #Bilateral blur
# blur_img=cv.bilateralFilter(img,5,15,15)

# blur_img=cv.resize(blur_img,(750,500))
# cv.imshow("Blur",blur_img)
# cv.waitKey(0)

"""Bitwise Operators"""
# blank=np.zeros((600,600), dtype="uint8")
# rectangle = cv.rectangle(blank.copy(),(30,30),(570,570),255,thickness=cv.FILLED)
# circle=cv.circle(blank.copy(),(299,299),300,255,thickness=cv.FILLED)
# cv.imshow("Rectangle",rectangle)
# cv.imshow("Circle",circle)
# #AND
# bitwise=cv.bitwise_and(rectangle,circle)
# #OR
# bitwise=cv.bitwise_or(rectangle,circle)
# #XOR
# bitwise=cv.bitwise_xor(rectangle,circle)
# #NOT
# bitwise=cv.bitwise_not(rectangle)

# cv.imshow("Bitwise",bitwise)

# cv.waitKey(0)

"""Masking"""
# img=cv.imread(r"Images\human.jpg")

# blank=np.zeros(img.shape[:2],dtype="uint8")
# mask=cv.circle(blank, (img.shape[1]//2-30,img.shape[0]//2),100,255,-1)

# masked=cv.bitwise_and(img,img,mask=mask)
# cv.imshow("Masked",masked)
# cv.waitKey(0)

"""Histograms"""
img=cv.imread(r"Images\leaf.jpg")
# # gray hist
# gray = cv.cvtColor(img,cv.COLOR_BGRGRAY)
# cv.imshow("Gray",gray)
# #calculating histogram
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title("Histogram")
# plt.plot(gray_hist)
# plt.show()

# #color hist
# col = ['r','g','b']
# plt.figure()
# cv.imshow("Image",img)
# for i,col in enumerate(col):
#     hist=cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,color=col)
# plt.show()

# cv.waitKey(0)

"""Thresholding techniques"""
# img = cv.imread(r"Images/face.jpg")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Image",gray)
# # Simple thresholding
# threshold, thresh = cv.threshold(gray, 155,255,cv.THRESH_BINARY)
# cv.imshow("Threshold Binary", thresh)

# # Adaptive thresholding
# thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
# cv.imshow("Adaptive Threshold", thresh)


# cv.imshow("Masked", masked)
# cv.waitKey(0)

"""Edge detection """
# img=cv.imread(r"Images\face.jpg")
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# #laplacian
# lap=cv.Laplacian(gray,cv.CV_64F)
# lap=np.uint8(np.absolute(lap))
# cv.imshow("Laplacian",lap)

# #Sobel
# sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
# sobely = cv.Sobel(gray,cv.CV_64F,0,1)
# cv.imshow("SobelX",sobelx)
# cv.imshow("SobelY",sobely)
# combined = cv.bitwise_or(sobelx,sobely)
# cv.imshow("Combined",combined)

# #canny
# canny=cv.Canny(gray,150,195)
# cv.imshow("Canny",canny)

# cv.waitKey(0)