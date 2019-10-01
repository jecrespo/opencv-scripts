'''
Captura de imagenes de cámara: jidetech gtn-ptz2162-3x
compra: https://www.amazon.es/C%C3%A1mara-Domo-PTZ-POE-Vigilancia/dp/B0746FQGCZ

Script ejecutado cada minuto mediante cron
'''

#!/usr/bin/python

import requests
import time
import smtplib
from email.MIMEText import MIMEText

timestr = time.strftime("%Y%m%d-%H%M%S")

url_imagen = "http://192.168.1.18/jpgmulreq/1/image.jpg?key=0&lq=0" # El link de la imagen
nombre_local_imagen = "/var/images_cam/" + timestr + "-imagen.jpg" # El nombre con el que queremos guardarla

try: 
	imagen = requests.get(url_imagen).content
	with open(nombre_local_imagen, 'wb') as handler:
		handler.write(imagen)
except:
	msg = MIMEText("Error captura imagen")
	fromaddr = "mycamera@mydomain.com"
	toaddr = "myemail@mydomain.com"
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Error captura imagen"
	s = smtplib.SMTP('localhost')
	s.sendmail(fromaddr, toaddr, msg.as_string())
	s.quit()
