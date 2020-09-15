import os
import re
import time
import random
from multiprocessing import Process
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) Multiprocessing 을 활용한 크롤러
   ㄴ 각 process 가 저마다 위키피디아 내부 항목 링크를 무작위로 따라가면서 제목을 출력

2) [중요] Multithreading 과 달리 process 들이 전역변수 visited 를 공유하지 않음!!!
'''

def getLinks(bsObj):
	print('Getting links in {}'.format(os.getpid()))
	links = bsObj.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))
	return [link for link in links if link not in visited]


def scrape_article(path):
	visited.append(path)
	html = urlopen('https://en.wikipedia.org{}'.format(path))
	time.sleep(2)
	bsObj = BeautifulSoup(html, 'html.parser')
	title = bsObj.find('h1').get_text()
	print()
	print('Scraping {} in process {}'.format(title, os.getpid()))
	links = getLinks(bsObj)
	if len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs['href']
		print(newArticle)
		scrape_article(newArticle)


def main():
	processes = []
	processes.append(Process(target=scrape_article, args=('/wiki/Kevin_Bacon',)))
	processes.append(Process(target=scrape_article, args=('/wiki/Monty_Python',)))

	for p in processes:
		p.start()


visited = []

if __name__ == '__main__':
	main()
