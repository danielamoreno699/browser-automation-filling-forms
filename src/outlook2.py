import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from decouple import config
PASSWORD = config('PASSWORD')
sender = 'danielatest123@outlook.es'
receiver= 'danielamoreno699@gmail.com'
password = 'danielatestpython123456'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'this is the subject'

body = '''
<h2> This is a test email sent from Python </h2>
there are only 2 cats in the world
'''
mimetext = MIMEText(body, 'html') # plain text or html

message.attach(mimetext)

attach_path = './pic.jpg'
attach_file = open(attach_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attach_path)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()

server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()