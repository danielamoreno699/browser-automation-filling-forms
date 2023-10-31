
#sending email every 60sec

import yagmail
import time
import pandas


from decouple import config
SECRET_KEY = config('SECRET_KEY')



sender = 'demosdaniela123@gmail.com'
subject = "this is the subject"


yag = yagmail.SMTP(user=sender, password=SECRET_KEY)
df = pandas.read_csv('./contacts.csv', encoding='utf-8')

print(df)
# print(os.getcwd())
# print(sys.executable)

for index,row in df.iterrows():
   
    contents = f"""  
    hi {row['name']}, este un email generado por python script. no reponder.
    """

    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email sent successfully")

    
