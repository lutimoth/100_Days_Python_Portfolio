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
today = pd.Timestamp.now().strftime('%m-%d')
# 1. Update the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')

birthdays['birthdate'] = birthdays.apply(lambda x:dt.datetime.strptime("{0} {1}".format(x['month'], x['day']), "%m %d"),axis=1)
birthdays.to_csv('test_birthday.csv')
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
today_df = birthdays.loc[birthdays['birthdate'].dt.strftime('%m-%d').eq(today)]
# print(today_df)

for index, people in today_df.iterrows():
    letter = random.randint(0,2)
    name = people['name']
    print(name)
#     if letter == 0:
#         with open('./letter_1.txt') as letter:
#             standard_letter = letter.readlines()
#         standard_letter[0] = standard_letter[0].replace('[NAME]', name)
#     elif letter == 1:
#         with open('./letter_2.txt') as letter:
#             standard_letter = letter.readlines()
#         standard_letter[0] = standard_letter[0].replace('[NAME]', name)
#     else:
#         with open('./letter_3.txt') as letter:
#             standard_letter = letter.readlines()
#         standard_letter[0] = standard_letter[0].replace('[NAME]', name)


# # 4. Send the letter generated in step 3 to that person's email address.
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs='lutimoth@gmail.com', 
#             msg=f"Subject: Happy Birthday\n\n {standard_letter}")




