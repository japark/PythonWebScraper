from nltk import word_tokenize
from nltk import Text


# NLTK 분석은 항상 Text 객체로 시작!
tokens = word_tokenize('Here is some not very interesting text.')
print(tokens)
text = Text(tokens)
print(text)
