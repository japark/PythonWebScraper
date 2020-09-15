import re
import time
import random
import _thread
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) Multithreading 을 활용한 크롤러
   ㄴ 각 thread 가 저마다 위키피디아 내부 항목 링크를 무작위로 따라가면서 제목을 출력

2) 서버 부하를 줄이기 위해 time.sleep 같은 대기(wait)기능 사용을 고려할 것!!!
'''

def getLinks(thread_name, bsObj):
	print('Getting links in {}'.format(thread_name))
	links = bsObj.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))
	return [link for link in links if link not in visited]


def scrape_article(thread_name, path):
	visited.append(path)
	html = urlopen('https://en.wikipedia.org{}'.format(path))
	time.sleep(2)
	bsObj = BeautifulSoup(html, 'html.parser')
	title = bsObj.find('h1').get_text()
	print()
	print('Scraping {} in thread {}'.format(title, thread_name))
	links = getLinks(thread_name, bsObj)
	if len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs['href']
		print(newArticle)
		scrape_article(thread_name, newArticle)


visited = []

try:
   _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon',))
   _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python',))
except:
   print('Error: unable to start threads')

while 1:
	pass
