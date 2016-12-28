import twitter

api = twitter.Api(consumer_key="yo7TOsy8bdIu9ZlK7CdLnd0sN",
	consumer_secret="sRUFYMk16y1f3jLEsfOfs2S0t0zHDC8vmcaAixH3UVawdXXYFR",
	access_token_key="800131076622458881-36NJNS5xC5QIZH6BdB4bZIk0pRU902R",
	access_token_secret="m7apKLNWbTcbHABFbgK40G1w6ysfWAmASPPtp62GqyGVF")

statuses = api.GetUserTimeline('25073877', count=500)

with open('tweets.txt', 'w') as f:
	for status in statuses:
		f.write(status.text + '\n')

