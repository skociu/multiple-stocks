# Requirements
The following packages can be installed via pip if not already there \
pandas_datareader, pandas, numpy

# About the Script
The script pulls data from yahoo finance based on a ticker list that yahoo recognizes. You can modify the ticker list and change the start and end date in this file.

# The output of the script
The script initially gets monthly stock prices for the tickers specified and then calculates stock returns and standard deviations on them. The last steps print the results and create an folder (if it doesn't exist) named Excel with their data:
1. price data
2. stock returns
3. correlation matrix
4. covariance matrix
