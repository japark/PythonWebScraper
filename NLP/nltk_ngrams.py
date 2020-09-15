from nltk import bigrams, ngrams
from nltk import FreqDist
from nltk.book import *

'''
*** NOTE ***

1) nltk 패키지에서 제공하는 긴 글 텍스트들을 로드

	*** Introductory Examples for the NLTK Book ***
	Loading text1, ..., text9 and sent1, ..., sent9
	Type the name of the text or sentence to view it.
	Type: 'texts()' or 'sents()' to list the materials.
	text1: Moby Dick by Herman Melville 1851
	text2: Sense and Sensibility by Jane Austen 1811
	text3: The Book of Genesis
	text4: Inaugural Address Corpus
	text5: Chat Corpus
	text6: Monty Python and the Holy Grail
	text7: Wall Street Journal
	text8: Personals Corpus
	text9: The Man Who Was Thursday by G . K . Chesterton 1908

2) text1, ... , text9 각각은 Text 객체!
   ㄴ 단어들의 배열로 생각하면 됨
'''

# Average number of use per word
print('\n', '='*25, 'Average number of use per word', '='*25, '\n')
print(len(text6)/len(set(text6)))

# Frequency Distribution for words
print('\n', '='*35, 'Frequency Dist.', '='*35, '\n')
fdist = FreqDist(text6)
print(fdist.most_common(10))

# 2-grams(bi-grams)
print('\n', '='*40, '2-grams', '='*40, '\n')
ngs = bigrams(text6)
ngs_dist = FreqDist(ngs)
print(ngs_dist.most_common(10))
print(ngs_dist[('Sir', 'Robin')])

# General N-grams
print('\n', '='*40, 'N-grams', '='*40, '\n')
ngs = ngrams(text6, 4)
ngs_dist = FreqDist(ngs)
print(ngs_dist.most_common(10))
print(ngs_dist[(':', '[', 'singing', ']')])
