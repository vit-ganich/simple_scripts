import os
import time
import datetime
import smtplib


class DumpSearch(object):
        
    @staticmethod
    def start():
    	"""Searching the FG_DUMPS folder with dump files"""

        today = datetime.datetime.today()
        print( today.strftime("%d-%m-%Y. %H:%M:%S"))

        while True:
            #  Chech the existence of FG_DUMPS folder
            if(os.path.exists(path) == True):

                files_list = os.listdir(path)
                #  Sector clear, position under control
                if not files_list:
                    print (time.ctime() + " FG_DUMPS folder is empty")
                else:
                	#  Houston, we have a problem
                    print (files_list)
                    print(time.ctime())
                    #  Send email with notification
                    DumpSearch.mail(server, from_address, from_pass, address_list, str(files_list)) # send email + files_list
                    print("Warning! Dump has been created!!!!")
                    return
            else:
                print(time.ctime(), "FG_DUMPS is absent, all right")
                time.sleep(5) #wait 5 sec and repeat


        @staticmethod
        def mail(server, from_address, from_pass, address_list, msg, port = 25):
        	"""Sending email notification to the specified address"""

                smtp_mail = smtplib.SMTP(server,port)
                smtp_mail.starttls()
                smtp_mail.login(from_address, from_pass)
                smtp_mail.sendmail(from_address, address_list, msg)  
                smtp_mail.quit()


server = 'smtp.mail.ru'
from_address = "example@gmail.com"
from_pass = "password"
address_list=['example1@mail.ru', 'example2@mail.ru']
msg = "FG_DUMPS was created! Something went wrong((("
path = r"C:\\Windows\FG_DUMPS"
            

DumpSearch.start()