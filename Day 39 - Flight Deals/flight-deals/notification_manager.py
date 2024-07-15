# this class is responsible for sending notifications with the deal flight details.

import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.my_number = os.environ["MY_NUMBER"]
        self.virtual_number = os.environ["VIRTUAL_NUMBER"]
        self.account_sid = os.environ["ACCOUNT_SID"]
        self.auth_token = os.environ["AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=f"whatsapp: {self.virtual_number}",
            to=f"whatsapp: {self.my_number}",
        )
        print(message.sid)
