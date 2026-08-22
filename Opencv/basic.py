import cv2 as cv
def rescale(frame,scale=0.1):
    #image,video and Live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img=cv.imread('Photo/anime-cityscape-sunset.jpg')
img2=rescale(img)
cv.imshow('Senami',img2)
#converting to grayscale
gray=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#blur- increase blur,increase kelsize
blur=cv.GaussianBlur(img2,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
#Edge Cascade
canny=cv.Canny(img2,125,175)
cv.imshow('canny',canny)
#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilate',dilated)
#eroding
erode=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded',erode)
#rescale
resized=cv.resize(img,(500,600),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)
#cropping
cv.imshow('corpped img',img2)
cv.waitKey(0)
