key = "yourkey"
secret = "yoursecret"
from bittrex import Bittrex
from bittrex import API_V2_0
my_bittrex = Bittrex(key, secret)

# Get Markets
markets = my_bittrex.get_markets()
marketsdf = pd.DataFrame.from_dict(markets['result'])
# Get Currencies
currencies = pd.DataFrame.from_dict(my_bittrex.get_currencies()['result'])
currencies_list = currencies[currencies['IsActive'] == True]['Currency'].unique()
# Get Ticker
ticker = my_bittrex.get_ticker('BTC-LTC')
print ticker['result'].head()
# Get Market Summaries
summaries = my_bittrex.get_market_summaries()
summariesdf = pd.DataFrame.from_dict(summaries['result'])
print summariesdf.head()
# Get Market Summary
summary = my_bittrex.get_marketsummary('BTC-LTC')
summarydf = pd.DataFrame.from_dict(summary['result'])
print summarydf.head()
# Get Orderbook
orderbook = my_bittrex.get_orderbook('BTC-LTC')
orderbookbuydf = pd.DataFrame.from_dict(orderbook['result']['buy'])
orderbookselldf = pd.DataFrame.from_dict(orderbook['result']['sell'])
print orderbookbuydf.head()
print orderbookselldf.head()
# Get Market History
history = my_bittrex.get_market_history('BTC-LTC')
historydf = pd.DataFrame.from_dict(history['result'])
print historydf.head()
