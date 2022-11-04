import requests
import lxml
from bs4 import BeautifulSoup

ACCEPT_LANGUAGE = 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

URL = 'https://www.amazon.com/Wera-05135926001-Nut-Drivers/dp/B00TJ3J81Q/'

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

result = requests.get(URL, headers=headers)
soup = BeautifulSoup(result.text, "lxml")
price_html = soup.find(class_="a-price-whole")
price = int(price_html.get_text().strip('.'))

print(price)