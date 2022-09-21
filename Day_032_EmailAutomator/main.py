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

# Filter dataframe for only birthdays which match today
today_df = birthdays.loc[birthdays['birthdate'].dt.strftime('%m-%d').eq(today)]

# Function which will help us rewrite letter template
def letter_fixer(letter_number):
    global letter
    with open(f'./letter_templates/letter_{letter_number}.txt') as letter_file:
        letter = letter_file.read()
        letter= letter.replace('[NAME]', name)
    return letter

# For each birthday in the dataframe, iterate and pick a random letter template
for index, people in today_df.iterrows():
    name = people['name']
    email = people['email']
    letter_fixer(random.randint(1,3))
    
# Send letter to person's address
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject: Happy Birthday\n\n {letter}")




