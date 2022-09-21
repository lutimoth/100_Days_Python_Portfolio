import smtplib
import os

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password=password)