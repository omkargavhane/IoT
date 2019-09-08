import serial
from time import sleep,ctime
import csv
from reserve import *
import threading as th
try:
    serobj=serial.Serial("/dev/ttyACM0",9600)
    #print('Serial Communication Started...')
except Exception:
    print("Check Port...")
#print("connected to ARDUINO...")
old_data=''         
def pyserial_thread():
    global old_data
    while True:
        try:
            if serobj.inWaiting()>0:
                try:
                    data=str(serobj.readline())
                except serial.serialutil.SerialException:
                    print("connection refused!!!")
                if len(data)==11:
                    data=data[2:6]
                    if data!=old_data:
                        #print('\t'+data)
                        with open("iot.csv","a",newline="") as fp:
                            wo=csv.writer(fp)
                            wo.writerow([ctime(),data])
                        old_data=data
        except Exception:
            print('CLOSING SERIAL COMMUNICATION...[ok]')
            break

pyth=th.Thread(target=pyserial_thread)
#imapthread=th.Thread(target=create_imapobj)
reserve_thread=th.Thread(target=menu)
#imapthread.start()
#print('IMAP_THREAD...[STARTED]')
#imapthread.join()
#print('IMAP_THREAD [COMPLETED]')
print('SERIAL_COMMUNICATION_THREAD...[STARTED]')
pyth.start()
reserve_thread.start()
print('RESERVATION_THREAD...[STARTED]')
reserve_thread.join()
#print('RESERVATION_THREAD...[COMPLETED]')
#pyth.join()
#print('SERIAL_COMMUNICATION_THREAD...[COMPLETED]')
#while input()!='SERIAL_CLOSE':
#    pass
