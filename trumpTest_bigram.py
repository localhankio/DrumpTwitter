from collections import defaultdict
from random import choice, randint
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import FreqDist, bigrams
from nltk.collocations import * 
from nltk.corpus import state_union
import re

str1 = """There once was a girl who decided to kill herself. No wait, that's too dark. Let me start again. There once was a girl 
		who decided to kill monsters that came into her head after a night of heavy drinking becasue of she was an alcaholic.
		There there, her mother said, trying to comfort her. Howerver, she was not convinced that the world was her oyster."""


def getCorpus():
	"""
	returns the corpus to use, should return a text file or a 
	corpus given by nltk
	"""
	sample = open("tweets.txt", "r", encoding="utf-8").read()
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
	randFirst = randint(0, totalWords)
	leftover = totalWords - randFirst
	print("leftover =", leftover)
	for key, value in wordCountDict.items():
		leftover -= value
		if (leftover <=0):
			return key

def buildSentence(wordCountDict, bigramDefDict, totalWords):
	"""To lazy to add documentation"""
	sentenceList = []
	for i in range(0,5):
		seedWord = getSeedWord(wordCountDict, totalWords)
		firstWord = seedWord # will only be seed word for first iteration
		generatedSentence = firstWord + " "
		for i in range(0,10):
			secondWord = choice(bigramDefDict[firstWord])
			#print("Second word ", secondWord)
			generatedSentence += secondWord + " "
			firstWord = secondWord
		sentenceList.append(generatedSentence)
	return sentenceList

def main():
	bigramCounts = defaultdict(int)
	baseCorpus = getCorpus()
	tokensList = tokenizeWords(baseCorpus)
	wordCount = getTotalWords(tokensList)
	corpusBigramsList = getBigrams(tokensList)
	corpusBigramDict = createBigramDict(bigramCounts, corpusBigramsList)
	sampleSents = buildSentence(bigramCounts, corpusBigramDict, wordCount)
	print("****Sample Sentences****\n")
	for sent in sampleSents: 
		print("\t",sent)
	print("\n****Sample Sentences****")


if __name__ == '__main__':
	main()