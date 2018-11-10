import serial
from time import sleep,ctime
import csv
try:
	serobj=serial.Serial("/dev/ttyACM0",9600)
except Exception:
	print("check port!!!")
#print("connected to ARDUINO...")

while True:
	if serobj.inWaiting()>0:
		try:
			data=str(serobj.readline())
		except serial.serialutil.SerialException:
			print("connection refused!!!")
		if len(data)==11:
			data=data[2:6]
			print(data)
			with open("iot.csv","a",newline="") as fp:
				wo=csv.writer(fp)
				wo.writerow([ctime(),data])



