# this class is responsible for sending notifications with the deal flight details.

import os
import smtplib
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.smtp_address = os.environ["VIRTUAL_EMAIL"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.my_number = os.environ["MY_NUMBER"]
        self.virtual_number = os.environ["VIRTUAL_NUMBER"]
        self.account_sid = os.environ["ACCOUNT_SID"]
        self.auth_token = os.environ["AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)
        self.connection = smtplib.SMTP(self.smtp_address)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=self.virtual_number,
            to=self.my_number,
        )
        print(message.sid)

    def send_email(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{email_body}".encode("utf-8")
                )
