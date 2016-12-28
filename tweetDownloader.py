import twitter

api = twitter.Api(consumer_key="",
	consumer_secret="",
	access_token_key="",
	access_token_secret="")

statuses = api.GetUserTimeline('25073877', count=500)

with open('tweets.txt', 'w') as f:
	for status in statuses:
		f.write(status.text + '\n')

