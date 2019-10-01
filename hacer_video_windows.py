#!/usr/local/bin/python2.7

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

img=[]
ruta = './images'
for arch in sorted(listdir(ruta)):
	if (isfile(join(ruta,arch))):
		print(join(ruta,arch))
		img.append(cv2.imread(join(ruta,arch)))

height,width,layers=img[1].shape
fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
#video = cv2.VideoWriter('output.avi',fourcc, 30.0,(640,480),True)
video=cv2.VideoWriter('video.avi',fourcc,30.0,(width,height),True)

for frame in img:
    video.write(frame)

video.release()
cv2.destroyAllWindows()
