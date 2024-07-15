import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]

# ------------------------- Tesla Stock -------------------------
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": STOCK_API_KEY,
}

response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# yesterday
yesterday_closing_price = data_list[0]["4. close"]
yesterday_price = float(yesterday_closing_price)

# day before yesterday
day_before_closing_price = data_list[1]["4. close"]
day_before_price = float(day_before_closing_price)

print(f"Yesterday closing price: {yesterday_price}\nBefore yesterday closing price: {day_before_price}")

difference = yesterday_price - day_before_price
print(f"Difference: {round(difference, 3)}")

up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

# percentage
percentage = (difference / yesterday_price) * 100
print(f"Percentage: {round(percentage, 3)}%")

# ------------------------- Tesla News -------------------------

# abs - only positive number
if abs(percentage) > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    new_response = requests.get("https://newsapi.org/", params=news_parameters)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [(f"{STOCK_SYMBOL}: {up_down}{percentage}%\n"
                           f"Headline: {article['title']}.\n"
                           f"Brief: {article['description']}") for article in three_articles]

    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    virtual_number = os.environ["VIRTUAL_NUMBER"]
    my_number = os.environ["MY_NUMBER"]

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=virtual_number,
            to=my_number,
        )
        print(message.sid)
