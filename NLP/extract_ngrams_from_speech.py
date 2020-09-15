import re
import string
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup


def cleanSentence(sentence):
	sentence = sentence.split(' ')
	sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
	sentence = [word for word in sentence if len(word) > 1
		or (word.lower() == 'a' or word.lower() == 'i')]
	return sentence


def cleanInput(content):
	content = content.upper()
	content = re.sub('\n', ' ', content)
	content = bytes(content, "UTF-8")
	content = content.decode("ascii", "ignore")
	# 문장 단위로 분할(마침표 뒤에 공백이 나타나는 것을 기준)
	sentences = content.split('. ')
	return [cleanSentence(sentence) for sentence in sentences]


# 출현빈도가 높지만 큰 의미를 갖지 않는 단어들을 포함한 N-grams 제외
def isCommon(ngram):
	commonWords = [
		'THE', 'BE', 'AND', 'OF', 'A', 'IN', 'TO', 'HAVE',
		'IT', 'I', 'THAT', 'FOR', 'YOU', 'HE', 'WITH', 'ON',
		'DO', 'SAY', 'THIS', 'THEY', 'IS', 'AN', 'AT', 'BUT',
		'WE', 'HIS', 'FROM', 'THAT', 'NOT', 'BY', 'SHE', 'OR',
		'AS', 'WHAT', 'GO', 'THEIR', 'CAN', 'WHO', 'GET', 'IF',
		'WOULD', 'HER', 'ALL', 'MY', 'MAKE', 'ABOUT', 'KNOW',
		'WILL', 'AS', 'UP', 'ONE', 'TIME', 'HAS', 'BEEN', 'THERE',
		'YEAR', 'SO', 'THINK', 'WHEN', 'WHICH', 'THEM', 'SOME',
		'ME', 'PEOPLE', 'TAKE', 'OUT', 'INTO', 'JUST', 'SEE',
		'HIM', 'YOUR', 'COME', 'COULD', 'NOW', 'THAN', 'LIKE',
		'OTHER', 'HOW', 'THEN', 'ITS', 'OUR', 'TWO', 'MORE',
		'THESE', 'WANT', 'WAY', 'LOOK', 'FIRST', 'ALSO', 'NEW',
		'BECAUSE', 'DAY', 'MORE', 'USE', 'NO', 'MAN', 'FIND',
		'HERE', 'THING', 'GIVE', 'MANY', 'WELL'
	]
	for word in ngram:
		if word in commonWords:
			return True
	return False


def getNgramsFromSentence(content, n):
	output = []
	for i in range(len(content)-n+1):
		if not isCommon(content[i:i+n]):
			output.append(content[i:i+n])
	return output


# N-gram 들의 리스트와 빈도를 같이 반환
def getNgrams(content, n):
	content = cleanInput(content)
	ngrams_count = Counter()
	ngrams_list = []
	for sentence in content:
		newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)]
		ngrams_list.extend(newNgrams)
		ngrams_count.update(newNgrams)
	return ngrams_list, ngrams_count

'''
Extract N-grams from a speech of William Henry Harrison
'''
url = 'https://pythonscraping.com/files/inaugurationSpeech.txt'
content = str(urlopen(url).read(), 'utf-8')
ngrams_list, ngrams_count = getNgrams(content, 2)
print(ngrams_count)
