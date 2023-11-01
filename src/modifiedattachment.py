
#sending email every 60sec

import yagmail
import time
import pandas


from decouple import config
SECRET_KEY = config('SECRET_KEY')



sender = 'demosdaniela123@gmail.com'
subject = "this is the subject"


yag = yagmail.SMTP(user=sender, password=SECRET_KEY)
df = pandas.read_csv('./contacs1.csv', encoding='utf-8')

print(df)
# print(os.getcwd())
# print(sys.executable)

def generate_file(filename, content):
    with open(filename, 'w') as f:
        f.write(str(content))

for index,row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    amount = row['amount']
    receiver_email = row['email']

    generate_file(filename, amount)

    
    subject = "this is the subject"
    contents = [f"""  
    hi {name}, you have to pay {amount}, name.
    """, filename]

    yag.send(to=receiver_email, subject=subject, contents=contents)
    print("Email sent successfully")

    
