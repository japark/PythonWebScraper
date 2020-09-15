import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 람다 표현식을 이용한 태그 추출
   ㄴ 람다 함수를 find, find_all 에 인자로 대입

2) 여기서의 람다 함수는 태그 객체를 인자로 받고, Boolean 을 반환해야 한다!
'''

url = 'http://www.pythonscraping.com/pages/page3.html'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
print()

# 속성이 두 개인 태그들을 추출
print(bs.find_all(lambda tag: len(tag.attrs) == 2))

print('\n' + '='*100 + '\n')

# 비슷하면서도 다른 차이에 주목!!!
# 첫번째 : Tag 들의 리스트, 두번째 : NavigableString 들의 리스트
print(bs.find_all(lambda tag: tag.get_text() == '\nVegetable Basket\n'))
print()
print(bs.find_all('', text='\nVegetable Basket\n'))
