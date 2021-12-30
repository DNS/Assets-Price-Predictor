https://query1.finance.yahoo.com/v7/finance/quote?fields=regularMarketPrice&symbols=LPPF.JK


https://query1.finance.yahoo.com/v8/finance/chart/LPPF.JK?interval=2m
https://query1.finance.yahoo.com//v8/finance/chart/LPPF.JK?symbol=AAPL&period1=0&period2=9999999999&interval=3mo
# Possible inputs for &interval=: 1m, 5m, 15m, 30m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    https://query1.finance.yahoo.com/v8/finance/chart/AAPL?symbol=AAPL&period1=0&period2=9999999999&interval=1d&includePrePost=true&events=div%7Csplit


-------------------

query1.finance.yahoo.com HTTP/1.0
query2.finance.yahoo.com HTTP/1.1 (difference between HTTP/1.0 & HTTP/1.1)

If you plan to use a proxy or persistent connections use query2.finance.yahoo.com

-------------------

# Yahoo has gone to a Reactjs front end which means if you analyze the request headers from the client to the backend you can get the actual JSON they use to populate the client side stores.

https://query1.finance.yahoo.com/v10/finance/quoteSummary/LPPF.JK?modules=

# Inputs for the ?modules= query:

    [
       'assetProfile',
       'summaryProfile',
       'summaryDetail',
       'esgScores',
       'price',
       'incomeStatementHistory',
       'incomeStatementHistoryQuarterly',
       'balanceSheetHistory',
       'balanceSheetHistoryQuarterly',
       'cashflowStatementHistory',
       'cashflowStatementHistoryQuarterly',
       'defaultKeyStatistics',
       'financialData',
       'calendarEvents',
       'secFilings',
       'recommendationTrend',
       'upgradeDowngradeHistory',
       'institutionOwnership',
       'fundOwnership',
       'majorDirectHolders',
       'majorHoldersBreakdown',
       'insiderTransactions',
       'insiderHolders',
       'netSharePurchaseActivity',
       'earnings',
       'earningsHistory',
       'earningsTrend',
       'industryTrend',
       'indexTrend',
       'sectorTrend',
	]


---------------

# important

summaryDetail
incomeStatementHistory
incomeStatementHistoryQuarterly
balanceSheetHistory
balanceSheetHistoryQuarterly
cashflowStatementHistory
cashflowStatementHistoryQuarterly
earnings
earningsHistory
earningsTrend
calendarEvents



