##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# Set up email environment
# Get today's date
my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')
today = pd.Timestamp.now().strftime('%m-%d')

# Read the CSV of all birthdays
birthdays = pd.read_csv('birthdays.csv')

# Convert separate month and days into singular birthdate
birthdays['birthdate'] = birthdays.apply(lambda x:dt.datetime.strptime("{0} {1}".format(x['month'], x['day']), "%m %d"),axis=1)
birthdays.to_csv('test_birthday.csv')

# Filter dataframe for only birthdays which match today
today_df = birthdays.loc[birthdays['birthdate'].dt.strftime('%m-%d').eq(today)]

# Function which will help us rewrite letter template
def letter_fixer(letter_number):
    global final_letter
    with open(f'./letter_templates/letter_{letter_number}.txt') as letter:
        standard_letter = letter.readlines()
    standard_letter[0] = standard_letter[0].replace('[NAME]', name)
    final_letter = ' '.join(standard_letter)
    return final_letter

# For each birthday in the dataframe, iterate and pick a random letter template
for index, people in today_df.iterrows():
    letter = random.randint(0,2)
    name = people['name']
    email = people['email']
    if letter == 0:
        letter_fixer(1)
    elif letter == 1:
        letter_fixer(2)
    else:
        letter_fixer(3)

# Send letter to person's address
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject: Happy Birthday\n\n {final_letter}")




