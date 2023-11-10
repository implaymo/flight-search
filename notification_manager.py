from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ["account_sid"]
        self.auth_token = os.environ["auth_token"]
        self.twilio_num = os.environ["twilio_num"]
        self.my_num = os.environ["my_num"]


    def send_message(self, city):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(body=f"These flights got cheaper!\n{city}", from_=self.twilio_num, to=self.my_num)
        print(message.status)

