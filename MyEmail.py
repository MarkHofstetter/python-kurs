import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = MIMEText("das ist mein emailtext")

msg['Subject'] = 'The contents of'
msg['From'] = 'me@bla.com'
msg['To'] = 'you@bli.at'

# Send the message via our own SMTP server.

print(msg)

#host='', port=0, local_hostname=None, [timeout, ]source_address=None)
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()