def test_run():
	import datetime
	from pandas_datareader import data
	import pandas as pd
	import numpy as np
	import os

	####################### CONFIGURATION - LIST OF TICKERS #################
	tickers = ['AMZN', 'SPY', 'M']
	start_date = datetime.datetime(2007,5,13)
	end_date = datetime.datetime(2017,5,13)
	#end_date = datetime.datetime.now()
        #start_date = end_date - datetime.timedelta(days=3650)
	###############################################################################################

	listall = []
	for ticker in tickers:
	    #Selecting the Adj Close column
	    mydata = data.get_data_yahoo(ticker,
	                                 start = start_date,
	                                 end = end_date,
	                                 interval='d')['Adj Close']
	    #Renaming the series with the ticker name and adding all the series into one list
	    symbol = pd.Series(mydata, name=ticker)
	    listall.append(symbol) 

	#Converting the price data into one list using Transpose
	df = pd.DataFrame(data=listall).T             
	print "price data", df, '\n'

	pctstocks = df.pct_change()
	print "Stock returns", pctstocks, '\n'

	cormat = pctstocks.corr()
	print "correlation matrix \n\n", cormat,"\n"

	covmat = pctstocks.cov()
	print "variance-covariance matrix \n\n", covmat,"\n"

	means = (1 + pctstocks.mean())**(12.0) - 1
	print  "Annual means \n\n", means, "\n"

	stdev = pctstocks.std()* np.sqrt(12)
	print  "Annual standard deviation \n\n", stdev, "\n"

	#initial weights add up to 1 - they are setup initially
	#as a division of 1/nr of tickers
	weights = [1/float(len(tickers))]*(len(tickers))
	weights = pd.Series(data=weights, index=tickers)
	print  "weights \n\n", weights, "\n"

	#Converting into arrays
	w1 = np.array(weights)
	m1 = np.array(means)
	cov1 = np.array(covmat)

	#Matrix multiplication for portfolio return
	#multiplying by 12 for annualized returns
	portret = np.dot(w1.T , m1)*(12.0)
	print  "portfolio return \n\n", portret , "\n"

	#Calculating portfolio standard deviation using equal weights,
	#covariance table 
	first = np.dot(w1.T, cov1)
	portstd = np.sqrt(np.dot(first,w1))*(12.0)
	print  "portfolio standard deviation \n\n", portstd , "\n"


	#check if directory Excel exists
	if os.path.isdir('./Excel') == False:
	    os.mkdir('./Excel')

	#creating csv files using the results
	cur_dir = os.path.dirname(__file__)
	df.to_csv(os.path.join(cur_dir, 'Excel//mystocks_prices.csv'))
	pctstocks.to_csv(os.path.join(cur_dir,'Excel//mystocks_pctchange.csv'))
	cormat.to_csv(os.path.join(cur_dir, 'Excel//mystocks_correlations.csv'))
	covmat.to_csv(os.path.join(cur_dir, 'Excel//mystocks_varcov.csv'))

if __name__ == "__main__":
    test_run()
