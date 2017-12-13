import requests
import pandas as pd


# COINMARKET CAP  
def get_coinmarketcap(rank_limit):
	url = 'https://api.coinmarketcap.com/v1/ticker/'
	r = requests.get(url).json()
	df = pd.DataFrame(r)
	df['rank'] = df['rank'].astype('int') 

	df[['percent_change_1h',
    	'percent_change_24h',
    	'percent_change_7d']] = df[['percent_change_1h',
        	                        'percent_change_24h',
            	                    'percent_change_7d']].astype('float')
	table = df[df['rank'] <=rank_limit]
	table[['name',
    	   'symbol',
       	   'price_usd',
       	   'percent_change_1h',
           'percent_change_24h',
           'percent_change_7d',
           'rank']].sort_values(['percent_change_24h'],
           	ascending=False).set_index(['rank'])
    return table


import gdax
# GDAX 
# BTC - USD
# ETH - USD
# LTC - USD
def get_gdax_order_book(pair):
	return client.get_product_order_book(pair)
def get_24_hour_stats(pair):
	return public_client.get_product_24hr_stats(pair)
# BlOCKCHAIN.INFO 
def get_total_btc():
    url ='https://blockchain.info/q/totalbc'
    return float(requests.get(url).json())
def get_total_unconfirmed_transactions():
    url = 'https://blockchain.info/q/unconfirmedcount'
    return float(requests.get(url).json())
def get_block_count():
    url = 'https://blockchain.info/q/getblockcount'
    return float(requests.get(url).json())



# BITCOIN AVERAGE 
def bitcoin_avg_tickers():
	url = 'https://apiv2.bitcoinaverage.com/constants/symbols'
	return requests.get(url).json()
def get_ticker_data(market,symbol): # market type = global or local
	url = 'https://apiv2.bitcoinaverage.com/indices/{market}/ticker/{symbol}'.format(market=market,symbol=symbol)
	data = reqeusts.get(url).json()
	return data
def get_historical_data(market,symbol,period):
    # Market Options = global or local
    # period = daily, monthly, alltime
    url = 'https://apiv2.bitcoinaverage.com/indices/{market}/history/{symbol}?period={period}&format=json'.format(market=market,symbol=symbol,period=period)
    data = requests.get(url).json()
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time')
    return df  

