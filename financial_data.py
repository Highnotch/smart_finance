import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

sia = SentimentIntensityAnalyzer()

def fetch_news():
    url = ('https://newsapi.org/v2/everything?'
       'q=Finance&'
       'from=2024-02-1&'
       'sortBy=popularity&'
       'apiKey=fcb3a8f25d0945ea9e3cd1e867f8df28')

    response = requests.get(url)
    news_data = response.json()["articles"]

    return news_data

def analyze_sentiment(news_data):
    for news in news_data:
        title_sentiment = sia.polarity_scores(news["title"])
        if "description" in news and news["description"] is not None:
            content_sentiment = sia.polarity_scores(news["description"])
            combined_sentiment = {
                "title_sentiment": title_sentiment["compound"],
                "content_sentiment": content_sentiment["compound"]
            }
            news.update(combined_sentiment)
        else:
            news.update({"title_sentiment": 0.0, "content_sentiment": 0.0})
    return news_data

def fetch_social_sentiment():
    social_sentiment = np.random.uniform(-1, 1, 10)
    return social_sentiment

def get_recommendation(sentiment_score):
    if sentiment_score >= 0.05:
        return "Positive sentiment: Consider investing in related assets."
    elif sentiment_score <= -0.05:
        return "Negative sentiment: Exercise caution with related investments."
    else:
        return "Neutral sentiment: Monitor the situation for further developments."
