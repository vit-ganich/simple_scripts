import sys, os
import smtplib
import glob
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_mail(address_book, strFrom):
    '''
    simple smtp mail sender 
    '''
    smtp = smtplib.SMTP(server)
    msgRoot = MIMEMultipart('related')

    #  Text + current date & time
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

    #  send email
    smtp.sendmail(strFrom, address_book, msgRoot.as_string())
    smtp.quit()

#  Kerio
server = '192.168.80.40'
strFrom = 'test@ts.local'
address_book = ['qa@ts.local']

#  Exchange
## server = '192.168.0.173'
## strFrom = 'admin@fg2.a'
## address_book = ['test4@fg2.a']


for item in range (2):
	date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
	#send mail
	send_mail(address_book, strFrom)
	print("mail #%s" % item)