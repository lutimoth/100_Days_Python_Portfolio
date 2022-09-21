##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')


# 1. Update the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')
birthdays = birthdays.replace('12', '9')
birthdays = birthdays.replace('21','20')

birthdays['birthdate'] = birthdays.apply(lambda x:dt.datetime.strptime("{0} {1} {2}".format(x['year'],x['month'], x['day']), "%Y %m %d"),axis=1)

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
today = dt.datetime.now()

if today in birthdays['birthdate']:
    letter = random.randint(0,2)
    name = birthdays.loc[birthdays['birthdate'] == today, ['name']].values()
    if letter == 0:
        with open('./letter_1.txt') as letter:
            standard_letter = letter.readlines()
        standard_letter[0] = standard_letter[0].replace('[NAME]', name)
    elif letter == 1:
        with open('./letter_2.txt') as letter:
            standard_letter = letter.readlines()
        standard_letter[0] = standard_letter[0].replace('[NAME]', name)
    else:
        with open('./letter_3.txt') as letter:
            standard_letter = letter.readlines()
        standard_letter[0] = standard_letter[0].replace('[NAME]', name)


# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='lutimoth@gmail.com', 
            msg=f"Subject: Happy Birthday\n\n {standard_letter}")




