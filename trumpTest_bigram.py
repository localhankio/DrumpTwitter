from collections import defaultdict
from random import choice, randint
import nltk
from nltk.tokenize import word_tokenize
from nltk import FreqDist, bigrams
from nltk.collocations import * 
from nltk.corpus import state_union

str1 = """There once was a girl who decided to kill herself. No wait, that's too dark. Let me start again. There once was a girl 
		who decided to kill monsters that came into her head after a night of heavy drinking becasue of she was an alcaholic.
		There there, her mother said, trying to comfort her. Howerver, she was not convinced that the world was her oyster."""


def getCorpus():
	# train = state_union.raw("2005-GWBush.txt")
	# sample = state_union.raw("2006-GWBush.txt")
	#finder = BigramCollocationFinder.from_words(sample.words('english-web.txt'))
	sample = open("./Manifesto.txt", "r", encoding="utf-8").read()
	return sample

def tokenizeWords(aCorpus):
	tokens = word_tokenize(aCorpus)
	return tokens

def getTotalWords(tokenizedWordsList):
	return len(tokenizedWordsList)

def getBigrams(tokensList):
	genBigrams = bigrams(tokensList)
	allBigrams = list(genBigrams)
	#print("***Bigram liset***\n", allBigrams, "\n***Bigram list***")
	return allBigrams

def createBigramDict(bigramDict, bigramList):
	anotherBigramDict = {}
	for first, second in bigramList:
		bigramDict[first] +=1
		anotherBigramDict.setdefault(first, []).append(second)
	return anotherBigramDict

def buildSentence(wordCountDict, bigramDefDict, totalWords):
	seedWord = getSeedWord()
	tempWord = seedWord
	sentences = []
	randFirst = randint(0, totalWords)
	leftover = totalWords - randFirst
	print("leftover =", leftover)
	for key, value in wordCountDict.items():
		leftover -= value
		#print("\tleft leftover", leftover)
		if (leftover <=0):
			chosenTok = key
			print(key)
			break
	for i in range(0,5):
		firstWord = getSeedWord()# will only be seed word for first iteration
		generatedSentence = firstWord + " "
		for i in range(0,10):
			secondWord = choice(bigramDefDict[firstWord])
			#print("Second word ", secondWord)
			generatedSentence += secondWord + " "
			firstWord = secondWord
		sentences.append(generatedSentence)
	return sentences

def getSeedWord():
	return "The"

def main():
	bigramCounts = defaultdict(int)
	baseCorpus = getCorpus()
	tokensList = tokenizeWords(baseCorpus)
	wordCount = getTotalWords(tokensList)
	corpusBigramsList = getBigrams(tokensList)
	corpusBigramDict = createBigramDict(bigramCounts, corpusBigramsList)
	sampleSents = buildSentence(bigramCounts, corpusBigramDict, wordCount)
	print("****Sample Sentence****\n")
	for sent in sampleSents: 
		print("\t",sent)
	print("\n****Sample Sentence****")


if __name__ == '__main__':
	main()