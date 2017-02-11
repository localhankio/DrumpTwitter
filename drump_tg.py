from collections import defaultdict
from random import choice, randint
import pickle 
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import trigrams 
import re


def getCorpus(corpus="./corpora/tweets.txt"):
	"""
	returns the corpus to use, should return a text file or a 
	corpus given by nltk
	"""
	try:
		sample = open(corpus, "r", encoding="utf-8").read()
	except Exception as e:
		raise e
	return sample

def tokenizeWords(aCorpus):
	"""
	tokenizes words with nltk's word_tokenize() method, 
	should update so it tokenizes according to twitter posts
	"""
	twitterTknzr = TweetTokenizer()
	tokens = twitterTknzr.tokenize(aCorpus)
	return tokens

def getTotalWords(tokenizedWordsList):
	"""returns number of words in a corpus"""
	return len(tokenizedWordsList)

def getTrigrams(tokensList):
	genTrigrams = trigrams(tokensList)
	return genTrigrams;

def createTrigramDict(trigramDict, trigramList):
	anotherTrigramDict = {}
	keyStr = ""

	for first, second, third in trigramList: 	
		keyStr = (first, second)
		#print(keyStr).encode('utf-8')
		trigramDict[keyStr] +=1
		anotherTrigramDict.setdefault(keyStr, []).append(third)
	return anotherTrigramDict

def isTokenPunctionation(token):
	'''
	finds if given token is punctionation, returns true if it is
	'''
	if (len(token) >=2 ):
		return False 
	elif (len(token) == 1 ):
		unicodeVal = ord(token)
		if (unicodeVal <= 47 or (unicodeVal >= 58 and unicodeVal <= 63)): #hardcoded numbers are unicode digits for punctionation, ignores "@" symbole bc valid on twitter
			# print("\tfound a punctionation", token)
			return True 
		else: 
			# print("\tNot punct for character ")
			return False  

def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
   
    step1 = words.replace("`` ", '"').replace(" ''", '"').replace('. . .',  '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
         "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()

def getSeedWord(wordCountDict, totalWords):
	'''returns a "seedword," or the first workd the tweet should start with'''
	seed = ":"
	firstToken = ""
	secondToken = ""
	while(isTokenPunctionation(seed)):  # while the seed word is NOT punctionation 
		randFirst = randint(0, totalWords)
		leftover = totalWords - randFirst
		for key, value in wordCountDict.items():
			firstToken = key[0]
			secondToken = key[1]
			leftover -= value
			if (leftover <=0):
				if(isTokenPunctionation(firstToken) ^ isTokenPunctionation(secondToken)):
					return ("MAKE", "AMERICA")
				elif (isTokenPunctionation(firstToken) and isTokenPunctionation(secondToken)): 
					return ("ObamaCare", "was")
				else: 
					return key

def buildTweet(wordCountDict, trigramDefDict, totalWords, tweetLength):
	"""To lazy to add documentation"""

	firstBigram = getSeedWord(wordCountDict, totalWords)  # will only be seed word for first iteration
	firstGivenToken = firstBigram[0]
	secondGivenToken = firstBigram[1]
	generatedTweet = firstGivenToken + " " + secondGivenToken + " "
	for j in range(0, tweetLength):
		thirdToken = choice(trigramDefDict[firstBigram])
		firstGivenToken = secondGivenToken
		secondGivenToken = thirdToken
		generatedTweet += thirdToken + " "
		firstBigram = (firstGivenToken, secondGivenToken)
	return generatedTweet
	
def readTrigrams(pickleLoc= "./trigrams.pickle"):
	trigrams = pickle.load(open(pickleLoc, "rb"))
	return trigrams

def generateTweets(wordCountDict, trigramDefDict, totalWords, numTweets=6):
	tweetLengths = [16, 17, 18, 18, 19, 20] #hard coded number of tokens in tweets, Trump averages 18.77 tokens tweets. picked a skewed distribution for token length 
	tweetList = []
	for i in range(0, numTweets):
		aFakeTweet = buildTweet(wordCountDict, trigramDefDict, totalWords, tweetLengths[i])
		tweetList.append(untokenize(aFakeTweet))
	return tweetList


def doEverything(corpusLoc="./corpora/tweets.txt", trigramPickleLoc="./corpora/trigrams.pickle"):
	'''
	Literally do all the things. Easy function to generate tweets
	@param corpus, the text file to base potential tweets 
	'''
	trigramCounts = defaultdict(int)
	corpusTrigramList = readTrigrams(trigramPickleLoc)
	wordCount = len(corpusTrigramList)
	corpusTrigramDict = createTrigramDict(trigramCounts, corpusTrigramList)
	sents = generateTweets(trigramCounts, corpusTrigramDict, wordCount, 5)
	return sents 
	# print("****Sample Sentences****\n")	
	# for sent in sampleSents: 
	# 	print("\t",sent)
	# print("\n****Sample Sentences****")

def main():
	tweets = doEverything()
	print(tweets)
	# print("****Sample Sentences****\n")
	# for sent in sampleSents: 
	# 	print("\t",sent)
	# print("\n****Sample Sentences****\n") 
	
if __name__ == '__main__':
	main()