
# run every day

import http_post_get as crawler
import re, sqlite3, time


websites = [
	'https://trends.google.com/',
	'https://finance.yahoo.com/',
	'https://www.msn.com/en-us/money/markets/marketmovers',
]

#text_res = crawler.http_get(websites[1])
#print(text_res)

#print(websites)

s = 'a,b,c,d,e'
m = re.split(',', s)

print(m)


