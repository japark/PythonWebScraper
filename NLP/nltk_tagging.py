from nltk import word_tokenize, sent_tokenize
from nltk import pos_tag

'''
*** NOTE ***

1) pos_tag 를 이용한 tagging

2) 같은 단어여도 tag 를 통해 그 의미나 역할을 구분
   ㄴ 예를 들면, dust 가 명사로 쓰였는지, 동사로 쓰였는지 파악

3) Tag 를 이용하면 정교한 웹 크롤링/스크래핑 가능
   ㄴ 특정 단어가 특정 용도로 쓰인 경우에만 스크랩 하는 등
'''

# 1) pos_tag 를 이용한 tagging
print('\n', '='*40, 'How to Attach Tags', '='*40, '\n')
text = word_tokenize('You see, in this world there\'s two kinds of people, \
	my friend: Those with loaded guns and those who dig. You dig.')
print(text, '\n')
words = pos_tag(text)
print(words)

# 2) NLTK tells the two "dust"s.
print('\n', '='*35, 'Difference btw dust and dust', '='*35, '\n')
text = word_tokenize('The dust was thick so he had to dust.')
words = pos_tag(text)
print(words)

# 3) Find the sentences where "Google" is used as a noun
print('\n', '='*30, 'Elaborate Targetting the word "Google"', '='*30, '\n')
sentences = sent_tokenize('Google is one of the best companies in the world. \
	I constantly google myself to see what I\'m up to.')
nouns = ['NN', 'NNS', 'NNP', 'NNPS']
print(sentences)
print()
for sentence in sentences:
	if 'google' in sentence.lower():
		taggedWords = pos_tag(word_tokenize(sentence))
		for word in taggedWords:
			if word[0].lower() == 'google' and word[1] in nouns:
				print(sentence)
