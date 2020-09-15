import re
import random
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 웹페이지에서 링크를 찾아 이동하는 크롤러 예시
   ㄴ 특정 위키백과 항목 페이지에서 다른 항목에 대한 링크들을 추출
   ㄴ 무작위로 하나를 선택하여 들어간 후, 위 작업 반복

2) 무한히 계속되지 않게 횟수제한 필요
'''

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
	bs = BeautifulSoup(html, 'html.parser')
	return bs.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))


i, times = 0, 10
links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0 and i < times:
	newArticle = links[random.randint(0, len(links)-1)].attrs['href']
	print(newArticle)
	links = getLinks(newArticle)
	i += 1
