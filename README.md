#Requirements
The following packages can be installed via pip if not already there
pandas_datareader, pandas, numpy

#About the Script
The script pulls data from yahoo finance based on a ticker list that yahoo recognizes. You can modify the tickert list and change the start and end date in this file.

#The output of the script
The script initially gets daily stock prices for the tickers specified and then calculates stock returns and standard deviations on them. I default weights to 1/number of tickers in the portfolio list. For example: Assuming there are four tickers in your tickers list, the weight calculated will be 25% (1/4)
After this the script calculates the portfolio return and the portfolio standard deviation using matrix multiplication.

The last steps print the results and create an folder (if it doesn't exist) named Excel with the data for:
1. price data
2. stock returns
3. correlation matrix
4. covariance matrix
