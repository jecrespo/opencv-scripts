'''
Concatenar videos capturados
'''

#!/usr/local/bin/python2.7

import cv2
import numpy as np
import os

videofiles = [n for n in os.listdir('/var/videos_cam')]
videofiles = sorted(videofiles)

video_index = 0
cap = cv2.VideoCapture('/var/videos_cam/'+videofiles[0])

image = cv2.imread("/var/images_cam/20181213-152801-imagen.jpg") #tamaño de una de las imagenes capturadas
height,width,layers=image.shape
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('/var/videos_cam/video_completo.avi',fourcc,15.0,(width,height),True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        print "end of video " + str(video_index) + " .. next one now"
        video_index += 1
        if video_index >= len(videofiles):
            break
        cap = cv2.VideoCapture('/var/videos_cam/'+videofiles[ video_index ])
        ret, frame = cap.read()
    #cv2.imshow('frame',frame)
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

print "end."
