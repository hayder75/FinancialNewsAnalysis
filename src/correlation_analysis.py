import pandas as pd

def normalize_dates(news_df, stock_df):
    """Align dates in both news and stock datasets."""
    # Convert 'date' columns to datetime without expecting timezone information
    news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')  # No UTC conversion
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')  # No UTC conversion

    # Drop rows with NaT values if any conversion failed
    news_df.dropna(subset=['date'], inplace=True)
    stock_df.dropna(subset=['Date'], inplace=True)

def calculate_daily_returns(stock_df):
    """Calculate daily returns from closing prices."""
    stock_df['Daily_Returns'] = stock_df['Close'].pct_change()

def aggregate_sentiments(news_df):
    """Aggregate sentiments by date."""
    return news_df.groupby('date')['sentiment'].mean().reset_index()

def correlation_analysis(aggregated_sentiments_df, stock_df):
    """Calculate correlation between sentiment scores and daily returns."""
    # Ensure both datetime columns are timezone-naive
    aggregated_sentiments_df['date'] = aggregated_sentiments_df['date'].dt.tz_localize(None)
    stock_df['Date'] = stock_df['Date'].dt.tz_localize(None)

    # Merge the dataframes
    merged_df = pd.merge(
        aggregated_sentiments_df,
        stock_df[['Date', 'Daily_Returns']],
        left_on='date',
        right_on='Date',
        how='inner'
    )

    # Calculate the correlation
    correlation = merged_df['sentiment'].corr(merged_df['Daily_Returns'])
    return correlation

