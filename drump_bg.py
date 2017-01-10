from collections import defaultdict
from random import choice, randint
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import bigrams
from nltk.collocations import * 
from nltk.corpus import state_union
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

def getBigrams(tokensList):
	"""
	given a corpus, returns a list of bigrams as a list of tuples
	"""
	genBigrams = bigrams(tokensList)
	allBigrams = list(genBigrams)
	#print("***Bigram liset***\n", allBigrams, "\n***Bigram list***")
	return allBigrams

def createBigramDict(bigramDict, bigramList):
	"""
	creates a dictionary with a count of each unique words
	"""
	anotherBigramDict = {}
	for first, second in bigramList:
		bigramDict[first] +=1
		anotherBigramDict.setdefault(first, []).append(second)
	return anotherBigramDict

def isTokenPunctionation(token):
	'''
	finds if given token is punctionation, returns true if it is
	'''

	if (len(token) >=2 ):
		return False 
	elif (len(token) == 1 ):
		unicodeVal = ord(token)
		if (unicodeVal <= 47 or (unicodeVal >= 58 and unicodeVal <= 63)): #hardcoded numbers are unicode digits for punctionation, ignores "@" symbole bc valid on twitter
			print("\tfound a punctionation")
			return True 
		else: 
			print("\tNot punct for character ")
			return False 
def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .',  '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
         "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()

def getSeedWord(wordCountDict, totalWords):
	print("getting seed word")
	'''returns a "seedword," or the first workd the tweet should start with'''
	seed = "!"
	while(isTokenPunctionation(seed)):  # while the seed word is NOT punctionation 
		randFirst = randint(0, totalWords)
		leftover = totalWords - randFirst
		for key, value in wordCountDict.items():
			leftover -= value
			if (leftover <=0):
				if (len(key) == 1):
					seed = key
					break 
				else:
					return key 
	return seed
def buildSentences(wordCountDict, bigramDefDict, totalWords, numTweets=6):
	"""To lazy to add documentation"""
	tweetLengths = [16, 17, 18, 18, 19, 20] #hard coded number of tokens in tweets, Trump averages 18.77 tokensa tweets
	sentenceList = []
	for i in range(0, numTweets):
		seedWord = getSeedWord(wordCountDict, totalWords)
		firstWord = seedWord # will only be seed word for first iteration
		generatedSentence = [firstWord]
		for j in range(0, tweetLengths[i]):
			secondWord = choice(bigramDefDict[firstWord])
			#print("Second word ", secondWord)
			generatedSentence.append(secondWord)
			firstWord = secondWord
		sentenceList.append(untokenize(generatedSentence))
	return sentenceList
	
def tryme():
	return "from trumpTest!"

def doEverything(corpus="./corpora/tweets.txt"):
	'''
	Literally do all the things. Easy function to generate tweets
	@param corpus, the text file to base potential tweets 
	'''
	bigramCounts = defaultdict(int)
	baseCorpus = getCorpus(corpus)
	tokensList = tokenizeWords(baseCorpus)
	wordCount = getTotalWords(tokensList)
	corpusBigramsList = getBigrams(tokensList)
	corpusBigramDict = createBigramDict(bigramCounts, corpusBigramsList)
	sents = buildSentences(bigramCounts, corpusBigramDict, wordCount, 5)
	return sents 
	# print("****Sample Sentences****\n")
	# for sent in sampleSents: 
	# 	print("\t",sent)
	# print("\n****Sample Sentences****")

def main():
	bigramCounts = defaultdict(int)
	baseCorpus = getCorpus()
	tokensList = tokenizeWords(baseCorpus)
	wordCount = getTotalWords(tokensList)
	corpusBigramsList = getBigrams(tokensList)
	corpusBigramDict = createBigramDict(bigramCounts, corpusBigramsList)
	sampleSents = buildSentences(bigramCounts, corpusBigramDict, wordCount, 6)
	print("****Sample Sentences****\n")
	for sent in sampleSents: 
		print("\t",sent)
	print("\n****Sample Sentences****\n")
	# print(corpusBigramDict["("])
if __name__ == '__main__':
	main()