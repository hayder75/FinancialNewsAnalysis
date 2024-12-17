import os
import pandas as pd
from textblob import TextBlob

def load_news_data(file_path):
    """Load financial news data from a CSV file."""
    return pd.read_csv(file_path)

def perform_sentiment_analysis(headlines):
    """Calculate sentiment scores for each headline."""
    return [TextBlob(headline).sentiment.polarity for headline in headlines]

def analyze_publishers(news_data):
    """Analyze the number of articles per publisher."""
    return news_data['publisher'].value_counts()

def analyze_publication_dates(news_data):
    """Analyze publication dates to identify trends over time."""
    # Parse dates with mixed timezone formats
    news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce', utc=True)
    
    # Drop rows with invalid or unparseable dates
    news_data = news_data.dropna(subset=['date'])
    
    # Convert to naive datetime (removing timezone info)
    news_data['date'] = news_data['date'].dt.tz_localize(None)
    
    # Extract just the date part and count occurrences
    return news_data['date'].dt.date.value_counts().sort_index()
