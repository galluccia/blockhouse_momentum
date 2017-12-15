from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Ripple"]
pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='', gprop='')
df = pytrends.interest_over_time()
df['Ripple'].plot(kind='line')
