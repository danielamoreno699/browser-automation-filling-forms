
#sending email every 60sec

import yagmail
import time
from datetime import datetime as dt

from decouple import config
SECRET_KEY = config('SECRET_KEY')

sender = 'demosdaniela123@gmail.com'
receiver = 'danielamoreno699@gmail.com'
subject = "this is the subject"

contents = """
Hello, this is a test email sent from Python using yagmail.
"""

while True:
    now = dt.now()
    if dt.now().hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=SECRET_KEY)
        yag.send(
        to=receiver,
        subject=subject,
        contents=contents)
        print("Email sent successfully")
        time.sleep(60)
