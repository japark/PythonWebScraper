from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 태그의 이름, 속성 등을 통해 원하는 태그들을 추출
   ㄴ find, find_all, get_text 등을 이용
   ㄴ 특히, find 와 find_all 메소드의 매개변수들에 대해 이해

2) https://www.pythonscraping.com/pages/warandpeace.html
   ㄴ 소설 "전쟁과 평화"의 일부가 담긴 웹페이지
   ㄴ 등장인물이 말하는 대사는 <span class="red"></span>으로,
	  등장인물 이름은 <span class="green"></span> 으로 둘러싸여 있다.
'''

url = 'https://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

print()

## span.green 태그를 모두 탐색
name_list = bs.find_all('span', {'class':'green'})
for name in name_list[:10]:
	print(name.get_text())  # name.text 도 같은 기능

print('\n' + '='*100 + '\n')

## h1 또는 h2 모두 탐색
print(bs.find_all(['h1', 'h2']))

print('\n' + '='*100 + '\n')

## span.red 또는 span.green 모두 탐색
print(bs.find_all('span', {'class':['red', 'green']})[:5])

print('\n' + '='*100 + '\n')

## "the prince"를 콘텐츠로 하는 모든 태그를 탐색
# Tag 가 아니라 NavigableString 들의 리스트를 반환!!!
print(bs.find_all(text='the prince'))

print('\n' + '='*100 + '\n')

## keywords parameter 이용
# print(bs.find(id='text'))
# class 속성의 경우, class_ 를 매개변수명으로 쓸 것!
print(bs.find(class_='green'))  # bs.find('', {'class':'green'}) 와 동일
