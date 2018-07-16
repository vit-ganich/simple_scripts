import sys, os
import smtplib
import glob
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")


def send_mail(address_book, attachments, strFrom):
    '''
    simple smtp mail sender 
    with attach founded files in attachments arg
    '''
    count = 1
    for file in attachments:
        smtp = smtplib.SMTP(server)
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
    
    	#  read file
        with open(file, 'rb') as fp:
            msg = MIMEBase('application', "octet-stream")
            msg.set_payload(fp.read())
        #  encoding
        encoders.encode_base64(msg)
        #  attach file
        msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
        msgRoot.attach(msg)

       	#  send email
        smtp.sendmail(strFrom, address_book, msgRoot.as_string())
        smtp.quit()
        #  print info
        print('message #%s, file "%s"' % (count, file))
        count += 1


server = 'smtp.mail.ru'
strFrom = 'fgqa.autotest@mail.ru'
address_book = ['ganich.test@mail.ru']

# path to attachments folder
#attachments = [item for item in glob.glob(r'\\192.168.1.99\it\IT_Falcongaze\STQA\Temp\Recognition_Files\11k_images\*.*')]
attachments = [item for item in glob.glob(r'C:\1\SMTP_ATTACH\Files\*.*')] #  <-------- PATH


#send mail
send_mail(address_book, attachments, strFrom)
