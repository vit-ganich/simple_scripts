# -*- coding: utf-8 -*-
from imapclient import IMAPClient
#  config file with user credentials for different accounts
from config_accounts import Gmail as MailAccounts


test_name = MailAccounts.test_name


def get_number_of_sent_emails(server,login,password,folder,test_name,message_body=[]):
    """
    Get an amount of sent messages to make sure 
    that emails were sent correctly
    """
    try:
        with IMAPClient(server) as client:
            client.login(login, password)
            #  Select the SENT folder
            client.select_folder(folder, readonly=False)
            #  Select ALL messages
            sent_messages = client.search(['ALL'])
            #  Read the message body
            try:
                #  Parsing raw http-messages into readable form and storing them in the list []
                message_body = [str(data[b'BODY[TEXT]']).split(";")[-1][39:-51]  #  [39:-51] for Gmail
                                for msgid, data in client.fetch(sent_messages, ['BODY[TEXT]']).items()]
            except:
                pass

        actual_result = len(sent_messages)
    except:
        actual_result = 'unknown'
    finally:
        with open(r'C:\Sikuli\log_DEBUG.txt','a') as f:
            f.write('------ %s.  Sent emails: %s\n%s\n' % (test_name, actual_result, message_body))

#  Credentials from the config
server = MailAccounts.server
login = MailAccounts.login
password = MailAccounts.password
folder = MailAccounts.folder


get_number_of_sent_emails(server, login, password, folder, test_name)
