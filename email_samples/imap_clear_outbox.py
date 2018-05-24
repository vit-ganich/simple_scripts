# -*- coding: utf-8 -*-
#import pprint
from imapclient import IMAPClient
#  config file with user credentials for different accounts
from config_accounts import Gmail as MailAccounts


test_name = MailAccounts.test_name


def clear_mailbox(server, login, password, folder, test_name):
    """
    Clear the SENT folder before sending emails
    """
    try:
        with IMAPClient(server) as client:
            client.login(login, password)
            #  get names of the mailbox folders
            #pprint.pprint(client.list_folders())
            
            client.select_folder(folder, readonly=False)
            client.delete_messages(client.search(['ALL']))
            client.expunge()
        err = ('OK')
    except:
        err = ('FAIL')
    finally:
        with open(r'C:\Sikuli\log_DEBUG.txt','a') as f:
            f.write('\n------ %s. Clearing Outbox - %s\n' % (test_name, err))

#  Credentials from the config
server = MailAccounts.server
login = MailAccounts.login
password = MailAccounts.password
folder = MailAccounts.folder


clear_mailbox(server, login, password, folder, test_name)