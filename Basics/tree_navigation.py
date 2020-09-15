from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 태그들의 상대적 관계를 통해 원하는 태그들을 추출
   ㄴ https://www.pythonscraping.com/pages/page3.html 페이지를 통해 확인

2) children, descendants,
   next_sibling, next_siblings,
   previous_sibling, previous_siblings
   parent, parents
'''

url = 'https://www.pythonscraping.com/pages/page3.html'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')


# 자식 태그들만 추출
for child in bs.find('table', {'id':'giftList'}).children:
	print(child)

print('='*100)

# 자손 태그들을 전부 탐색
for child in bs.find('tr', {'id':'gift5'}).descendants:
	print(child)

print('='*100)

# 형제 태그(동생 태그)들 추출
# next_sibling 은 가장 가까운 동생 태그 하나만 추출
for sibling in bs.find('tr', {'id':'gift3'}).next_siblings:
	print(sibling)

print('='*100)

# 형제 태그(형 태그)들 추출
# previous_sibling 은 가장 가까운 형 태그 하나만 추출
for sibling in bs.find('tr', {'id':'gift2'}).previous_siblings:
	print(sibling)

print('='*100)

# 부모 태그의 추출
# parents 는 계속 거슬러 올라가서 얻은 모든 부모 태그들을 추출
print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
