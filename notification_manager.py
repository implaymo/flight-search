# from twilio.rest import Client
# import os
# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     account_sid = os.environ["account_sid"]
#     auth_token = os.environ["auth_token"]
#     twilio_num = os.environ["twilio_num"]
#     my_num = os.environ["my_num"]
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(body="New price!", from_=twilio_num, to=my_num)
#
