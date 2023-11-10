from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.twilio_num = os.getenv("twilio_num")
        self.my_num = os.getenv("my_num")

    def send_message(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(body=message,
                                         from_=self.twilio_num, to=self.my_num)
        print(message.status)

