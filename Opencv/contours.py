import cv2 as cv

img=cv.imread('C:\Python\AI\Opencv\Photo\Senami.jpeg')
# cv.imshow('img',img)
resized=cv.resize(img,(400,600))
gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('black and white',gray)
canny=cv.Canny(gray,125,175)
cv.imshow('canny edges',canny)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
cv.waitKey(0)