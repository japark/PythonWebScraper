from random import randint
from urllib.request import urlopen

'''
Text Generation by Markov Model
'''

def wordListSum(wordList):
	summ = 0
	for word, value in wordList.items():
		summ += value
	return summ

def retrieveRandomWord(wordList):
	randIndex = randint(1, wordListSum(wordList))
	for word, value in wordList.items():
		randIndex -= value
		if randIndex <= 0:
			return word

def buildWordDict(text):
	# Remove newlines and quotes
	text = text.replace('\n', ' ')
	text = text.replace('"', '')

	# Make sure punctuation marks are treated as their own "words,"
	# so that they will be included in the Markov chain
	punctuation = [',','.',';',':']
	for symbol in punctuation:
		text = text.replace(symbol, ' {} '.format(symbol))

	words = text.split(' ')
	# Filter out empty words
	words = [word for word in words if word != '']

	wordDict = {}
	for i in range(1, len(words)):
		if words[i-1] not in wordDict:
			# Create a new dictionary for this word
			wordDict[words[i-1]] = {}
		if words[i] not in wordDict[words[i-1]]:
			wordDict[words[i-1]][words[i]] = 0
		wordDict[words[i-1]][words[i]] += 1
	return wordDict


url = 'https://pythonscraping.com/files/inaugurationSpeech.txt'
text = str(urlopen(url).read(), 'utf-8')
wordDict = buildWordDict(text)
# print(wordDict)

# Generate a Markov chain of length 100
length = 100
chain = ['I']
for i in range(0, length):
	newWord = retrieveRandomWord(wordDict[chain[-1]])
	chain.append(newWord)
print(' '.join(chain))
