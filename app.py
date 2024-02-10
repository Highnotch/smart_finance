from flask import Flask, render_template, request
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import pandas as pd
from openai_integration import generate_openai_recommendations
app = Flask(__name__)

# Function to fetch real-time financial news from an API
def fetch_news():
    url = ('https://newsapi.org/v2/everything?'
       'q=Finance&'
       'from=2024-02-1&'
       'sortBy=popularity&'
       'apiKey=fcb3a8f25d0945ea9e3cd1e867f8df28')

    response = requests.get(url)
    news_data = response.json()["articles"]

    return news_data

# Function to perform sentiment analysis on news articles
def analyze_sentiment(news_data):
    sia = SentimentIntensityAnalyzer()
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

# Main route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and perform analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']
    password = request.form['password']
    openai_key = request.form['openai_key']  # Retrieve OpenAI API key from form data
    
    # Fetch financial news and perform sentiment analysis
    news_data = fetch_news()
    analyzed_news = analyze_sentiment(news_data)
    df = pd.DataFrame(analyzed_news)
    
    # Process analysis results (here you can customize it according to your needs)
    analysis_results = []
    for _, row in df.iterrows():
        recommendation = generate_openai_recommendations(openai_key, row['financial_context'])
        analysis_results.append({
            "title": row['title'],
            "description": row['description'],
            "title_sentiment": row['title_sentiment'],
            "content_sentiment": row['content_sentiment'],
            "recommendation": recommendation
        })

    return render_template('index.html', username=username, password=password, analysis_results=analysis_results)
# Function to provide investment recommendations based on sentiment scores
def get_recommendation(sentiment_score):
    if sentiment_score >= 0.05:
        return "Positive sentiment: Consider investing in related assets."
    elif sentiment_score <= -0.05:
        return "Negative sentiment: Exercise caution with related investments."
    else:
        return "Neutral sentiment: Monitor the situation for further developments."

if __name__ == '__main__':
    app.run(debug=True)
