'''def random_att(attachments):
    mess_att = []
    for i in range(5):
        for item in range(4):
            mess_att.append(attachments[random.randint(0,len(attachments)-1)])

        print('message #%s, file "%s"' % (i, mess_att))
        mess_att.clear()




def random_att_2(attachments):
    mess_att = []
    for i in range(4,len(attachments),4):
        for item in range(4):
            mess_att.append(attachments[i-item])
        print('message #%s, file "%s"' % (i, mess_att))
        mess_att.clear()'''



import sys, os
import smtplib
import glob
import random
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")


def send_mail(address_book, attachments, strFrom, number_of_messages):
    '''
    simple smtp mail sender 
    with attach founded files in attachments arg
    '''

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Test mail Python %s' % date
    msgRoot['From'] = strFrom
    msgRoot['To'] = ','.join(address_book)
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # set mail body
    body = (r'<b>Images in attachment.</b><br><br> Date - {0} <br><br><br><br><br><br><br><br><i></i>').format(date)
    msgText = MIMEText(body, 'html')
    msgAlternative.attach(msgText)
    smtp = smtplib.SMTP(server)

    for i in range(number_of_messages):
        for item in range(4):
        		# Random file from selected folder
                file = attachments[random.randint(0,len(attachments)-1)]

                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                msgRoot.attach(msg)
       

        smtp.sendmail(strFrom, address_book, msgRoot.as_string())
        print('message #%s, file "%s"' % (count, msg))


    smtp.quit()

server = '192.168.0.173'
strFrom = 'admin@fg1.m'
address_book = ['ganich.test@mail.ru']
attachments = [item for item in glob.glob(r'C:\1\SMTP_ATTACH\Files\*.*')]

# How much messages?
number_of_messages = 100 # <------------ number of messages


#send mail
send_mail(address_book, attachments, strFrom, number_of_messages)