import cv2 as cv
import numpy as np
img=cv.imread('Photo/anime-cityscape-sunset.jpg')
img2=cv.resize(img,(800,600))
cv.imshow('city',img2)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
#-x -->left
#-y -->up
#x -->right
#y -->Down
translated=translate(img2,100,100)
cv.imshow('translated',translated)
#rotation
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img2,rotmat,dimensions)
rotated=rotate(img2,45)
cv.imshow('rotated',rotated)
#resize
resized=cv.resize(img2,(400,700),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)
#flip
flip=cv.flip(img2,-1)
cv.imshow('flip',flip)
#cropped
cropped=img2[200:300,400:500]
cv.imshow('cropped',cropped)
cv.waitKey(0)