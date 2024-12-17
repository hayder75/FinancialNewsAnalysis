import pandas as pd
import talib

def load_stock_data(file_path):
    """Load stock price data from a CSV file."""
    return pd.read_csv(file_path)

def prepare_stock_data(stock_data):
    """Prepare stock data by setting the date index."""
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.set_index('Date', inplace=True)
    return stock_data

def calculate_indicators(stock_data):
    """Calculate technical indicators using TA-Lib."""
    stock_data['SMA_20'] = talib.SMA(stock_data['Close'], timeperiod=20)
    stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)
    stock_data['MACD'], stock_data['MACD_signal'], _ = talib.MACD(stock_data['Close'])
    return stock_data

def visualize_stock_with_indicators(stock_data):
    """Visualize stock prices with technical indicators."""
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(14, 7))
    
    plt.subplot(3, 1, 1)
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['SMA_20'], label='20-Day SMA', color='orange')
    
    plt.subplot(3, 1, 2)
    plt.plot(stock_data['RSI'], label='RSI', color='purple')
    
    plt.subplot(3, 1, 3)
    plt.plot(stock_data['MACD'], label='MACD', color='blue')
    
    plt.tight_layout()
    plt.show()
