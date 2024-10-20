import numpy as np

def YahooData2returns(YahooData):
    # Yahoo Data = raw downloaded data from Yahoo Finance using yfinance
    # returns = % returns of 'Adj Close' as a data vector (not a data frame)

import yfinance as yf
import numpy as np
import pandas as pd

# Function to compute returns from Yahoo Finance data
def YahooData2returns(YahooData):
    # Extract 'Adj Close' column
    adj_close = YahooData['Adj Close']
    
    # Extract values from 'Adj Close' column and transform to a simple array (numpy array)
    pricevec = adj_close.values
    
    # Calculate the lagged returns (r_t = (P_t / P_(t-1)) - 1)
    returns = pricevec[1:] / pricevec[:-1] - 1
    
    return returns

# Function to download stock data using yfinance
def get_stock_data(symbol):
    # Download historical stock data for the symbol
    data = yf.download(symbol)
    
    # Return the full data (including 'Adj Close' column)
    return data

# Example usage:
# Download data for a stock symbol (e.g., Goldman Sachs - 'GS')
YahooData = get_stock_data('GS')

# Compute the returns using YahooData2returns function
returns = YahooData2returns(YahooData)

# Print the calculated returns
print(returns)
