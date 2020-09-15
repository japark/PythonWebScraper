import re
import os
import time
import random
from urllib.request import urlopen
from multiprocessing import Process, Queue
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) Multiprocessing 을 활용한 크롤러
   ㄴ 각 process 가 위키피디아 내부 항목 링크들을 크롤링하면서 제목을 출력
   ㄴ Processes 가 각자의 경로를 따라가는 것이 아니라, 함께 작업하여 웹사이트를 완전히 커버!

2) 여기서의 Queue 는 multithreading 에서 쓴 Queue (from queue import Queue) 와 다른 것
'''

def task_delegator(taskQueue, urlsQueue):
	visited = ['/wiki/Kevin_Bacon', '/wiki/Monty_Python']
	taskQueue.put('/wiki/Kevin_Bacon')
	taskQueue.put('/wiki/Monty_Python')

	while 1:
		# Check to see if there are new links in the urlsQueue for processing
		if not urlsQueue.empty():
			links = [link for link in urlsQueue.get() if link not in visited]
			for link in links:
				taskQueue.put(link)
				visited.append(link)


def get_links(bsObj):
	print('Getting links in {}'.format(os.getpid()))
	links = bsObj.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))
	return [link.attrs['href'] for link in links]


def scrape_article(taskQueue, urlsQueue):
	while 1:
		while taskQueue.empty():
			# Sleep 100 ms while waiting for the task queue 
			# This should be rare
			time.sleep(.1)
		path = taskQueue.get()
		html = urlopen('https://en.wikipedia.org{}'.format(path))
		time.sleep(2)
		bsObj = BeautifulSoup(html, 'html.parser')
		title = bsObj.find('h1').get_text()
		print()
		print('Scraping {} in process {}'.format(title, os.getpid()))
		links = get_links(bsObj)
		# Send these to the delegator for processing
		urlsQueue.put(links)


def main():
	processes = []
	taskQueue = Queue()
	urlsQueue = Queue()
	processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue,)))
	processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))
	processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))

	for p in processes:
		p.start()


if __name__ == '__main__':
	main()
