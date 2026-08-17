import cv2 as cv
def rescale(frame,scale=0.5):
    #image,video and Live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('Photo/Senami.jpeg')
img_resized=rescale(img)
cv.imshow('Senami',img_resized)
def changeres(width,height):
   #Live Video
   Capture.set(3,width)
   Capture.set(4,height)
Capture=cv.VideoCapture('Video/download_20260814_214443_0000.mp4')
while True:
    isTrue,frame=Capture.read()
    frame_resized=rescale(frame)
    """ cv.imshow('Video',frame) """
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
      break

Capture.release()
cv.destroyAllWindows() 
""" cv.waitKey(0) """