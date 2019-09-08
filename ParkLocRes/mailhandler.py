from smtplib import SMTP
#from getpass import getpass
from email.mime.text import MIMEText
import csv
import time
#smtpobj=''

def check_for_genuinereq(eid,opt):
    opt,res_time=opt.split()
    print(opt,res_time)
    today=time.localtime()
    today_date,cur_mon,cur_year,cur_hour=today.tm_mday,today.tm_mon,today.tm_year,today.tm_hour
    st,en=tuple(map(int,res_time.split('-')))
    if st<0 and st>24  and en<0 and en>24:
        return 'Invalid Arguments for time.\n Specify time in 24 HOUR format'
    print(st,cur_hour)
    if st<cur_hour:
        return 'Inavlid time range.'
    tot_slots=set((1,2,3,4))
    res_slots=set()
    with open('reserve.csv','r')as fp:
        ro=csv.reader(fp)
        data=list(ro)
    #print(data)
    if data:
        for e in data:
            str_time=time.strptime(e[1])
            store_date,store_mon,store_year=str_time.tm_mday,str_time.tm_mon,str_time.tm_year
            if store_date==today_date and store_mon==cur_mon and store_year==cur_year:
                int_res=set(range(int(e[-1].split('-')[0]),int(e[-1].split('-')[1])+1)).intersection(set(range(int(res_time.split('-')[0]),int(res_time.split('-')[1])+1)))
            #if e[-1]==res_time.split():
                #print(int_res)
                if len(int_res)>1:
                    res_slots.add(int(e[-2]))
    #print(res_slots)
        #print('[check_for_req_genuine_func] reserved slots:',res_slots)
    if tot_slots.intersection(res_slots)==tot_slots:
        print('[check_for_genuine_req] Sorry,All slots are reserved for timing {}'.format(res_time))
        return 'Sorry,All slots are reserved for timing {}'.format(res_time)
    else:
        slot_tobe_res=list(tot_slots-res_slots)[0]
        with open('reserve.csv','a') as fp:
            wo=csv.writer(fp)
            wo.writerow([eid,time.ctime(),slot_tobe_res,res_time])
        print('[check_for_genuine_req] slot_tobe_reserved:',slot_tobe_res)
        return 'Slot {} is reserved between {} for {}.\nDo pay while exiting the parking as per HOUR BASIS.'.format(slot_tobe_res,res_time,eid[:eid.find('@')])

def create_smtpobj():
    smtpobj=SMTP("smtp.gmail.com",587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login("pythonmailservice2358@gmail.com",'python_2358')
    print('[create_smtpobj] successfully login to smtp.gmail.server.')
    return smtpobj
#print("connected with server...")
#def status():
#rec=input("Enter Recipient's Email Address:")
def mysendmail(emailid,opt):
    smtpobj=create_smtpobj()
    if opt.lower()=='echo':
        with open("iot.csv","r") as fp:
            ro=csv.reader(fp)
            data=list(ro)[-1]
        availslot=0
        #print(data[-1])
        for e in data[-1]:
            if e=='0':availslot+=1
        with open('reserve.csv','r') as fp:
            ro=csv.reader(fp)
            rdata=list(ro)
            new_data=[]
            #print('rdata :',rdata)
            if rdata[0]:
                for e in rdata:
                    new_data.append(str([e[-2],e[-1]]))
            rdata='\n'.join(new_data)
        msg=MIMEText("""******[ SMART PARKING ]******\n\nThanks for echo request\n\n-->TIMESTAMP [{}]\n\n-->Total Parking Slots [4] as [0][1][2][3]\n\n-->Available Parking Slots[{}] are as [{}][{}][{}][{}]\n\n[NOTE]:where '0' indicates EMPTY SLOT\n\n[SLOTS | TIME<24HOUR>]\n{}\n\n[IMPORTANT]:TO reserve the slots make new message with SAME SUBJECT and message body will have  'reserve time' and time is 24 HOUR FORMAT\neg:reserve 10-12\n\nThanks for choosing us!!!.""".format(data[0],availslot,data[1][0],data[1][1],data[1][2],data[1][3],rdata))
        msg['subject']='Response to echo [ACK].'
        smtpobj.sendmail("pythonmailservice2358@gmail.com",emailid,msg.as_string())
        print('[Mail_handler] Mail Send to',emailid,'...[echo]')
    elif opt.lower().startswith('reserve'):
        ret=check_for_genuinereq(emailid,opt)
        msg=MIMEText(ret)
        msg['subject']="Respons to <reserve time> request."
        smtpobj.sendmail("pythonmailservice2358@gmail.com",emailid,msg.as_string())
        print('[Mail_handler] Mail Send to',emailid,'...[Reserve]')
    smtpobj.quit()
        #smtpobj.quit()
    #elif opt.startswith('reserve'):
                
