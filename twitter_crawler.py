from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

url = 'https://github.com/geduldig/TwitterAPI/tree/master/examples'

r = api.request('search/tweets', {'q':'pizza'})
for item in r:
        print(item)


r = api.request('statuses/filter', {'track':'pizza'})
for item in r.get_iterator():
    if 'text' in item:
        print item['text']