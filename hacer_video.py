'''
Hacer vídeo de las imagens capturadas en captura_imagenes_camara.py
'''

#!/usr/local/bin/python2.7

import cv2
import numpy as np
from os.path import isfile
import glob

img=[]
ruta = '/var/images_cam/'

#filtro de imagenes
#files = glob.glob(ruta+'20190319*.jpg')
files = glob.glob(ruta+'*.jpg')

for arch in sorted(files):
	if (isfile(arch)):
		print(arch)
		img.append(cv2.imread(arch))

height,width,layers=img[1].shape
fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
video=cv2.VideoWriter('/var/videos_cam/video.avi',fourcc,20.0,(width,height),True)

for frame in img:
    video.write(frame)

video.release()
cv2.destroyAllWindows()
