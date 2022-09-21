import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs='lutimoth@gmail.com', 
        msg="Subject: Hello \n\nOh what a test! Can we Python it?")