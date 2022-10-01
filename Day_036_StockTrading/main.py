import os
from dotenv import load_dotenv
from datetime import date, timedelta
import requests
from twilio.rest import Client

load_dotenv()

alpha_key = os.getenv('ALPHA_KEY')
news_key = os.getenv('NEWS_KEY')
twilio_sid = os.getenv('TWILIO_SID')
twilio_auth = os.getenv('TWILIO_AUTH')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CURRENT_DAY = date.today()
YESTERDAY = CURRENT_DAY - timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def price_change(today, yesterday):
    open = float(today['1. open'])
    close = float(yesterday['4. close'])
    change = (open-close/close) * 100
    if change > 5 or change < -5:
        get_news()
    return change

alpha_url = (f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_key}')
stock_request = requests.get(alpha_url)
data = stock_request.json()['Time Series (Daily)']
today_data = data[CURRENT_DAY.strftime('%Y-%m-%d')]
yesterday_data = data[YESTERDAY.strftime('%Y-%m-%d')]

percent_change = price_change(today_data, yesterday_data)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_url = (f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_key}&language=en')

def get_news():
    news_info = {}
    news_request = requests.get(news_url)
    news_data = news_request.json()['articles'][:3]
    for article in news_data:
        if article['source']['name'] not in news_info:
            news_info[article['source']['name']] = [article['title']]
        else:
            news_info[article['source']['name']] += [article['title']]
    send_message(news_info)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message(articles):
    client = Client(twilio_sid, twilio_auth)
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

get_news()

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

