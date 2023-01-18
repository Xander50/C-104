import cv2
img=cv2.imread("poster.jpg")
#cv2.imshow("display Image",img)
#print(img)

#gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("Gray scale",gray_img)
# print(gray_img)

rocket=img[120:360,400:500]

img[0:240,500:600]=rocket

text_to_show="I love coding"

cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.imshow("output",img)
cv2.waitKey(0)