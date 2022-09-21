import smtplib
import random
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')

today = dt.datetime.now()

if today.weekday() == 1:
    with open('quotes.txt') as quotes:
        quote_list = quotes.readlines()
        quote_list = [line.rstrip() for line in quote_list]
        today_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='lutimoth@gmail.com', 
            msg=f"Subject: Quote of the Day\n\n {today_quote}")

