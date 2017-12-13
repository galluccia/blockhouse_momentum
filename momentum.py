def get_supported_tickers():
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
    df.sort_values(['time'],ascending=True)
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time')
    return df

symbols = get_supported_tickers()['crypto']['symbols']

for symbol in symbols:
    

