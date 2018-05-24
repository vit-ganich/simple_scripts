# coding=utf-8
import time
from telethon import TelegramClient


class Telegram():
	'''
	This script sends files to selected users via Telegram API.
	You need to register your API for receiving API ID and API hash:
	https://core.telegram.org/api/obtaining_api_id
	'''

    def SendMessage(api_id, api_hash, phone, LocalUser,
                    Telegram_code, RemoteUser, file_path):
    
        client = TelegramClient(LocalUser, api_id, api_hash)
        client.connect()

        #  Authorization
        if not client.is_user_authorized():
            client.sign_in(phone=phone)
            me = client.sign_in(code=Telegram_code)

        #  Sending logs
        for file in file_path:
            for user in RemoteUser:
                client.send_file(user, file)
                time.sleep(2)

#  User credenrials
LocalUser = ## ID of telegram user
api_id = ## API ID
api_hash = ## API hash
phone = ## user phone

Telegram_code = ## Your login code. This code can be used to log in to your Telegram account
#  Remote users
RemoteUser = ['@user1', '@user2', '@user3']
#  Files list
file_path = [r'C:\log.txt', r'C:\log_DEBUG.txt']


Telegram.SendMessage(api_id, api_hash, phone, LocalUser,
                     Telegram_code, RemoteUser, file_path)