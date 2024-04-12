import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "CCEE433X0LF6HNU2"
NEWS_API = "034976fed149475e9d762ebdc34fdcc3"
TWILLO_ACCOUNT = "AC7e24286cf94c003dd07d3174521c66ca"
TWILLO_PASSWORD = "6ca5513a723e73c2b9b1f6c5b2d01a5e"
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_pram = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_pram)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference/float(yesterday_closing_price)) *100
if diff_percent > 1:
    news_pram = {
        "apikey" :NEWS_API,
        "qInTitle" :COMPANY_NAME,

    }
    response = requests.get(NEWS_ENDPOINT, params=news_pram)
    articles = response.json()["articles"]
    print(articles)
    three_articles = articles[:3]

    formatted_article = [f"Headline : {article['title']}. \ nBrief: {article['description']}" for  article in three_articles]

    client =Client(TWILLO_ACCOUNT, TWILLO_PASSWORD)
    for article in formatted_article:
        message = client.messages\
        .create(
            body=article,
            from_="+18065414294",
            to="+919068888371"
        )


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

