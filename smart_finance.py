import numpy as np
import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import openai

from authentication import authenticate_user
from financial_data import fetch_news, analyze_sentiment, fetch_social_sentiment, get_recommendation
from user_preferences import get_user_preferences
from portfolio_management import generate_portfolio, optimize_portfolio
from financial_goals import track_financial_goals
from life_events import adjust_strategies_for_life_events
from openai_integration import generate_openai_recommendations
from visualization import visualize_performance
from provide_financial_education import provide_financial_education

def smart_finance(username, password):
    if authenticate_user(username, password):
        news_data = fetch_news()
        analyzed_news = analyze_sentiment(news_data)
        df = pd.DataFrame(analyzed_news)
        user_preferences = get_user_preferences(username)
        for index, row in df.iterrows():
            print(f"Title: {row['title']}")
            print(f"Description: {row['description']}")
            print(f"Title Sentiment Score: {row['title_sentiment']:.2f}")
            print(f"Description Sentiment Score: {row['content_sentiment']:.2f}")
            print("Recommendation:", get_recommendation(row['content_sentiment']))
            print("User Preferences:", user_preferences)
            print("\n")
        social_sentiment = fetch_social_sentiment()
        if np.mean(social_sentiment) >= user_preferences["social_media_sentiment_threshold"]:
            print("Positive sentiment detected on social media. Consider adjusting investment strategies.")
        current_portfolio = generate_portfolio()
        optimized_portfolio = optimize_portfolio(user_preferences, current_portfolio)
        investment_performance = np.random.rand(100).cumsum() 
        investment_goals = user_preferences["investment_goals"]
        progress = track_financial_goals(investment_performance, investment_goals)
        visualize_performance(investment_performance, progress)
        education_resources = provide_financial_education(user_preferences)
        print("Personalized Financial Education Resources:")
        for resource, link in education_resources.items():
            print(f"{resource}: {link}")
        print("\n")
        adjusted_strategies = adjust_strategies_for_life_events(user_preferences, current_portfolio)
        print("Adjusted Investment Strategies for Life Events:")
        for event, portfolio in adjusted_strategies.items():
            print(f"{event}: {portfolio}")
        financial_context = user_preferences["financial_context"]
        openai_recommendations = generate_openai_recommendations(financial_context)
        print("Personalized Investment Recommendations (OpenAI):")
        print(openai_recommendations)
    else:
        print("Authentication failed. Please check your username and password.")

smart_finance("Sujith", "Krackhack")
