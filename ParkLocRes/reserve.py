import imapclient as ic
import pyzmail as pzm
import datetime
import time
#import pprint as pp
from mailhandler import create_smtpobj,mysendmail 
import threading  as th
SLEEP_TM=5
imapobj=''
#create imapclient object
def create_imapobj():
    imapobj=ic.IMAPClient('imap.gmail.com',ssl=True)
    #login to imap server
    imapobj.login('pythonmailservice2358@gmail.com','python_2358')
    #select folder from where message to be read
    print('[create_imapobj] SUCCESSFULLY LOGIN INTO IMAP.GMAIL SERVER...[ok]'.swapcase())
    #smtpthread=th.Thread(target=create_smtpobj)
    #smtpthread.start()
    #smtpthread.join()
    return imapobj
    #set filter for messages returns id's assosciated with mails

def menu(): 
    #imapthread.join()
    imapobj=create_imapobj()
    cnt=1
    print('[Thread Reserve] Waiting for requests...')
    while True:
        imapobj.select_folder('INBOX')
        uid=imapobj.search([u'UNSEEN',u'SUBJECT',u'parking locator'])
        if len(uid)>0:
            print('[Thread Reserve] Found requests:',len(uid))
            break
        time.sleep(SLEEP_TM)
    thread_in_menu=th.Thread(target=menu)
    thread_in_menu.start()
    print('[Thread Reserve] id:',uid)
    for e in uid:
        print('[Thread Reserve] inside for',e)
        #fetch body part of each uid
        rdata=imapobj.fetch(e,['BODY[]'])
        print('[Thread Reserve] body fetched for ',e)
        #parse the data
        parse_data=pzm.PyzMessage.factory(rdata[e][b'BODY[]'])
        print('[Thread Reserve] parsing of msg body ...[done]',e)
        msgfrom=parse_data.get_addresses('from')
        print('[Thread Reserve] from:',e,msgfrom)
        msgto=parse_data.get_addresses('to')
        print('[Thread Reserve] to:',e,msgto)
        subject=parse_data.get_subject()
        print('[Thread Reserve] subject:',e,subject)
        #print(subject)
        data=parse_data.text_part.get_payload().decode(parse_data.text_part.charset)[:-2]
        print('[Thread Reserve] Message:',e,data)
        #print(msgfrom,subject,msgto,data)
        if subject=='parking locator':
            if data.lower()=='echo':
                print('[Thread Reserve] found req...[echo]',msgfrom)
                mysendmail(msgfrom[0][1],data)
            elif data.lower().startswith('reserve'):
                print('[Thread Reserve] found req...[reservation]',msgfrom)
                mysendmail(msgfrom[0][1],data)
        #elif data.lower().startswith('reserve')'''
    imapobj.logout()
    #thraed_in_menu.join()
#while input()!='quit':
#    pass


    
