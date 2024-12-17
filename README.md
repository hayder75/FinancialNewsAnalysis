# Financial News Sentiment Analysis and Stock Movement Correlation

## Overview
This project aims to analyze financial news data to discover correlations between news sentiment and stock market movements. The analysis includes sentiment extraction from headlines, date normalization, and correlation analysis with stock price changes.

## Folder Structure
├── src/
│ ├── init.py
│ ├── task_1_analysis.py # Contains functions for loading news data and performing sentiment analysis
│ ├── task_2_analysis.py # Contains functions for loading stock data and calculating indicators
│ └── correlation_analysis.py # Contains functions for normalizing dates, aggregating sentiments, and performing correlation analysis
├── notebooks/
│ └── Task_1_Sentiment_Analysis.ipynb # Jupyter Notebook for Task 1
│ └── Task_2_Quantitative_Analysis.ipynb # Jupyter Notebook for Task 2
│ └── Task_3_Correlation_Analysis.ipynb # Jupyter Notebook for Task 3
├── requirements.txt # List of required packages
└── README.md # Project documentation


## Packages Used
- **pandas**: For data manipulation and analysis.
- **TextBlob**: For performing sentiment analysis on news headlines.
- **matplotlib**: For data visualization.
- **TA-Lib**: For calculating technical indicators in stock data (used in Task 2).

## Tasks Completed
1. **Task 1: Sentiment Analysis**
   - Loaded financial news data.
   - Performed sentiment analysis on headlines using TextBlob.
   - Analyzed publication trends by date.

2. **Task 2: Quantitative Analysis**
   - Loaded stock price data.
   - Calculated daily returns and technical indicators using TA-Lib.

3. **Task 3: Correlation Analysis**
   - Normalized dates to align news articles with stock trading days.
   - Aggregated sentiment scores by date.
   - Analyzed the correlation between average daily sentiment scores and daily stock returns.


