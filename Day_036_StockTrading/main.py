import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
import requests
from collections import defaultdict

load_dotenv()

alpha_key = os.getenv('ALPHA_KEY')
news_key = os.getenv('NEWS_KEY')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CURRENT_DAY = date.today()
YESTERDAY = CURRENT_DAY - timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def price_change(today, yesterday):
    open = float(today['1. open'])
    close = float(yesterday['4. close'])
    change = (abs(open-close)/close) * 100
    if change > 5:
        get_news()
    return change

alpha_url = (f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_key}')
stock_request = requests.get(alpha_url)
data = stock_request.json()['Time Series (Daily)']
today_data = data[CURRENT_DAY.strftime('%Y-%m-%d')]
yesterday_data = data[YESTERDAY.strftime('%Y-%m-%d')]

print(price_change(today_data, yesterday_data))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_url = (f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_key}&language=en')

def get_news():
    news_info = {}
    news_request = requests.get(news_url)
    news_data = news_request.json()['articles'][:3]
    #print(news_data)
    for article in news_data:
        if article['source']['name'] not in news_info:
            news_info[article['source']['name']] = [article['title']]
        else:
            news_info[article['source']['name']] += [article['title']]
        #print(news_info)
    return news_info

print(get_news())

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

