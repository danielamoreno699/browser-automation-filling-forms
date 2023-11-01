import smtplib

from decouple import config
PASSWORD = config('PASSWORD')
sender = 'danielatest123@outlook.es'
receiver= 'danielamoreno699@gmail.com'
password = 'danielatestpython123456'
message = """\
Subject: Hi there

This message is sent from Python.
I WANT TO SAY HELLO
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()