import requests
import os 
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup
import smtplib

### == Header info and item of interest == ###

ACCEPT_LANGUAGE = 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

URL = 'https://www.amazon.com/Wera-05135926001-Nut-Drivers/dp/B00TJ3J81Q/'
ITEM = 'Wera-05135926001-Nut-Drivers'
TARGET_PRICE = 100

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

### == Getting the Price from website == ###

result = requests.get(URL, headers=headers)
soup = BeautifulSoup(result.text, "lxml")
price_html = soup.find(class_="a-price-whole")
price = int(price_html.get_text().strip('.'))

#print(price)

### == Email if price drops == ##
load_dotenv()

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')

if price <= TARGET_PRICE:
     with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f"Subject: AMAZON PRICE ALERT!\n\nQuick! Your item {ITEM} is at or below your target price of ${TARGET_PRICE} and is currently ${price}. You can buy it here: {URL}")
