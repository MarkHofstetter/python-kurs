'''
def send_email_message(emailaddress, msgbody, subject):
   # was koennen sie
   # was haben sie
   
   

def send_sms_message(phonenumber, msgbody, subject(?)):


send_email_message()

send_sms_message()
'''

import WifiMessage

sms = WifiMessage.SMS

sms.body = 'hallo welt'
sms.phonenumber = '12345'

print(sms.body)

email = WifiMessage.WifiEmail
email.address = 'bla@blub.at'
email.body = 'hi all'
# email.send()
# print(email.address)