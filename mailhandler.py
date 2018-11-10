from smtplib import SMTP
from getpass import getpass
from email.mime.text import MIMEText
import csv
smtpobj=SMTP("smtp.gmail.com",587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login("pythonmailservice2358@gmail.com",getpass())
print("connected with server...")

while True:
	rec=input("Enter Recipient's Email Address:")
	with open("iot.csv","r") as fp:
		ro=csv.reader(fp)
		data=list(ro)[-1]
	availslot=0
	for e in data[1]:
		if e=='0':availslot+=1
	msg=MIMEText("""**TIMESTAMP[{}]\n\n**Total Parking Slots [4] as [0,1,2,3]\n\n**Available Parking Slots[{}] as [{},{},{},{}]\n\n
NOTE:where '0' indicates EMPTY SLOT\n\n\n\n Thanks for choosing us!!!\n :-) from Omkar Gavhane.""".format(data[0],availslot,data[1][0],data[1][1],data[1][2],data[1][3]))
	msg['Subject']="[IOT]PARKING_LOCATOR."
	if rec=="quit":break
	smtpobj.sendmail("pythonmailservice2358@gmail.com",rec,msg.as_string())
	print("Message Send To[",rec,"]",sep="")
smtpobj.quit()
