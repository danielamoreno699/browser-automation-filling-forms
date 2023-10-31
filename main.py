import yagmail
import  os

SECRET_KEY = os.environ.get('SECRET_KEY')

sender = 'danielamoreno699@gmail.com'
receiver = 'fokeme3065@hondabbs.com'
subject = "this is the subject"

contents = """
Hello,"""

yag = yagmail.SMTP(user=sender, password=SECRET_KEY) 
