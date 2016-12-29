import twitter
from keys import cons_key, cons_secret, access_sec, access_tok

api = twitter.Api(consumer_key=cons_key,
	consumer_secret=cons_secret,
	access_token_key=access_tok,
	access_token_secret=access_sec)

statuses = api.GetUserTimeline('25073877', count=500)

with open('tweets.txt', 'w') as f:
	for status in statuses:
		f.write(status.text + '\n')

