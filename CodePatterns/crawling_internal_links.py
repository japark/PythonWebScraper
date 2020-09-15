import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 재귀(recursion)를 활용한 크롤러 예시
   ㄴ 내부링크를 따라가는 크롤러를 활용하면 어떤 웹사이트의 전체구조 파악 가능

2) 위키피디아 최상위 페이지에서부터 모든 내부링크들을 탐색
   ㄴ https://en.wikipedia.org/wiki/Main_Page 에서 시작
   ㄴ 내부링크들을 빠짐없이 확인하면서 제목, 첫 문단, 편집링크주소 등을 추출

3) 위키피디아 웹사이트의 구조는 매우 크므로, 적당한 시점에서 프로그램 강제종료 필요
   ㄴ 특히, 재귀호출 횟수제한에 유의!!!
'''

def getLinks(pageUrl):
	html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
	bs = BeautifulSoup(html, 'html.parser')
	try:
		# 페이지의 제목
		print(bs.h1.get_text())
		# 페이지의 콘텐츠에서 첫 문단
		contents = bs.find(id ='mw-content-text').find_all('p')
		for content in contents:
			if content.get_text().strip(): break
		print(content)
		# 페이지를 편집하기 위한 링크주소
		print(bs.find('nav', id='p-lang').find('div', {'class':'body'})
			.find('a', class_='wbc-editpage').attrs['href'])
	except AttributeError:
		print('This page is missing something! Continuing.')

	for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
		if link.attrs['href'] not in pages:
			newPage = link.attrs['href']
			print('-'*100)
			print(newPage)
			pages.add(newPage)
			getLinks(newPage)


pages = set()
getLinks('')
