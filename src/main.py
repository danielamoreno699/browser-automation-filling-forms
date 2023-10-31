import yagmail

from decouple import config
SECRET_KEY = config('SECRET_KEY')

sender = 'demosdaniela123@gmail.com'
receiver = 'demosdaniela123@gmail.com'
subject = "this is the subject"

contents = """
Hello,
"""

yag = yagmail.SMTP(user=sender, password=SECRET_KEY)
yag.send(
    to=receiver,
    subject=subject,
    contents=contents,
)

print("Email sent successfully")
