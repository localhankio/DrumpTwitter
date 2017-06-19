#DrumpTwitter
Generates Hypothetical tweets that Donald Trump would post.
This application references his previous tweets to create hypothetical tweets. 
Since it only uses bigrams to generate sentneces, some the tweets generated may not make sense. Grammmar structure is not taken into account. It may be added in a later release.

##Command line tools
There is also a command-line utility to interface with the program. Please note that you need to have NLTK installed beforehand.
### Sample 
```
$ python drump_tg.py
****Sample Tweets****

         to bring back onto the boys. sells Taiwan billions of
         to incredible things will be allowed to get " DRAIN THE
         of the ratings machine, although @CNN and inaccurate and space
         the Lockheed Martin F - why have " Russian hacking defense
         of me accurately & FAR LESS MONEY on January 20th.

****Sample Tweets****
```
When running on command prompt in Windows, you may encounter ``UnicodeEncodeError`` when running the program. This is coasued byt the fact that cmd.ext is not encoding in UTF-8

##APIs used
* Flask v0.12
* NLTK v3.2.1
* Twitter-python
