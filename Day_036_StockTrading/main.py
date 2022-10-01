import os
from dotenv import load_dotenv
from datetime import date, timedelta
import requests
from twilio.rest import Client

load_dotenv()

STOCK_KEY = os.getenv('ALPHA_KEY')
NEWS_KEY = os.getenv('NEWS_KEY')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CURRENT_DAY = date.today()
YESTERDAY = CURRENT_DAY - timedelta(days=1)

STOCK_URL = 'https://www.alphavantage.co/query?'
NEWS_URL = 'https://newsapi.org/v2/everything?'

stock_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_KEY
}

news_params = {
    'q':COMPANY_NAME,
    'apiKey':NEWS_KEY,
    'language':'en'
}

percent_change = 0
stock_request = requests.get(STOCK_URL, params=stock_params)
data = stock_request.json()['Time Series (Daily)']

# Message sending function
def send_message(articles):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    if percent_change > 5:
        message = client.messages \
                    .create(
                        body= f"🔺TSLA: {percent_change}%",
                        from_='+17407154094',
                        to='+16266794568'
                    )
    if percent_change < 5:
        message = client.messages \
                    .create(
                        body= f"🔻TSLA: {percent_change}%",
                        from_='+17407154094',
                        to='+16266794568'
                    )
    print(articles)
    for agency in articles:
        for title in articles[agency]:
            message = client.messages \
                    .create(
                        body= f"{agency}: {title}",
                        from_='+17407154094',
                        to='+16266794568'
                    )

# News Gathering Function
def get_news():
    news_info = {}
    news_request = requests.get(NEWS_URL, params=news_params)
    news_data = news_request.json()['articles'][:3]
    for article in news_data:
        if article['source']['name'] not in news_info:
            news_info[article['source']['name']] = [article['title']]
        else:
            news_info[article['source']['name']] += [article['title']]
    send_message(news_info)

# Price Change Calculation Function
def price_change(today, yesterday):
    open = float(today['1. open'])
    close = float(yesterday['4. close'])
    change = ((open-close)/close) * 100
    if change > 5 or change < -5:
        get_news()
    return change

try:
    today_data = data[CURRENT_DAY.strftime('%Y-%m-%d')]
    yesterday_data = data[YESTERDAY.strftime('%Y-%m-%d')]
except KeyError:
    CURRENT_DAY, YESTERDAY = YESTERDAY, YESTERDAY - timedelta(days=1)
    today_data = data[CURRENT_DAY.strftime('%Y-%m-%d')]
    yesterday_data = data[YESTERDAY.strftime('%Y-%m-%d')]

percent_change = price_change(today_data, yesterday_data)
print(percent_change)

