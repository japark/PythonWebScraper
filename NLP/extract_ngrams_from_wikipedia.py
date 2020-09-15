import re
import string
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup


def cleanSentence(sentence):
	sentence = sentence.split(' ')
	sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
	# 정관사 a 나 I(나)는 한 글자 허용
	sentence = [word for word in sentence if len(word) > 1
		or (word.lower() == 'a' or word.lower() == 'i')]
	return sentence


def cleanInput(content):
	content = content.upper()
	# 줄바꿈 문자와 인용기호 제거 (ex : [12])
	content = re.sub('\n|\[[\d]+\]', ' ', content)
	content = bytes(content, "UTF-8")
	content = content.decode("ascii", "ignore")
	# 문장 단위로 분할(마침표 뒤에 공백이 나타나는 것을 기준)
	sentences = content.split('. ')
	return [cleanSentence(sentence) for sentence in sentences]


# 실질적으로 N-gram을 만드는 부분
def getNgramsFromSentence(content, n):
	output = []
	for i in range(len(content)-n+1):
		output.append(content[i:i+n])
	return output


# 진입점
# N-gram 들의 리스트와 빈도를 같이 반환
# 데이터 정규화 Data Normalization
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
Extract N-grams from a Wikipedia document
'''
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams_list, ngrams_count = getNgrams(content, 2)
print(ngrams_count, len(ngrams_count.keys()))
print('2-grams count is: '+str(len(ngrams_list)))
