import cv2 as cv
img=cv.imread('Photo/Senami.jpeg')
cv.imshow('Senami',img) 
#reading videos
'''Capture=cv.VideoCapture('Video/download_20260814_214443_0000.mp4')
while True:
    isTrue,frame=Capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
      break

Capture.release()
cv.destroyAllWindows()  '''  
cv.waitKey(0)