

import http_post_get as crawler
import re


all_res = crawler.http_get('https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=1&length=100')


for i in range(1,8):
	#print(i)
	all_res += crawler.http_get('https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start={}00&length=100'.format(i) )



s1 = re.findall(r'"Code":"(\w+?)"', all_res, re.MULTILINE | re.IGNORECASE | re.DOTALL)

if s1:
	print(s1)
else:
	print('error: not found')





'''
# fetch data
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=1&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=100&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=200&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=300&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=400&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=500&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=600&length=100
https://www.idx.co.id/umbraco/Surface/StockData/GetSecuritiesStock?start=700&length=100



'''
