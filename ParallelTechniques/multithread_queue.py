import re
import random
import time
import _thread
from urllib.request import urlopen
from queue import Queue
import pymysql
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) Multithreading 을 활용한 크롤러
   ㄴ 각 thread 가 저마다 위키피디아 내부 항목 링크를 무작위로 따라가면서 제목을 출력

2) 2개의 threads 에서 크롤링&스크래핑 진행, 1개의 thread 는 데이터베이스에 저장 담당
   ㄴ Queue 활용 (Queue : FIFO 혹은 LIFO 방식으로 작동하는 리스트 비슷한 객체)
   ㄴ 데이터베이스 인터페이스 구실을 하는 thread 몇 개를 따로 만들어 관리하는 것이 편리

3) 사용자 입력 사항
   - <database name> : 데이터베이스 이름을 입력
   - <table name> : 선택된 데이터베이스 안의 테이블 이름을 입력
   - passwd : 로컬 서버 비밀번호 입력
'''

def storage(queue):
	conn = pymysql.connect(host='127.0.0.1',
						   user='root',
						   passwd='',
						   db='mysql')
	cur = conn.cursor()
	cur.execute('USE <database name>')
	while 1:
		if not queue.empty():
			article = queue.get()
			cur.execute('SELECT * FROM <table name> WHERE path = %s', (article["path"]))
			if cur.rowcount == 0:
				print("Storing article {}".format(article["title"]))
				cur.execute('INSERT INTO <table name> (title, path) VALUES (%s, %s)',
					(article["title"], article["path"]))
				conn.commit()
			else:
				print("Article already exists: {}".format(article['title']))


def getLinks(thread_name, bsObj):
	print('Getting links in {}'.format(thread_name))
	links = bsObj.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))
	return [link for link in links if link not in visited]


def scrape_article(thread_name, path, queue):
	visited.append(path)
	html = urlopen('https://en.wikipedia.org{}'.format(path))
	time.sleep(2)
	bsObj = BeautifulSoup(html, 'html.parser')
	title = bsObj.find('h1').get_text()
	print()
	print('Added {} for storage in thread {}'.format(title, thread_name))
	queue.put({'title':title, 'path':path})
	links = getLinks(thread_name, bsObj)
	if len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs['href']
		print(newArticle)
		scrape_article(thread_name, newArticle, queue)


visited = []
queue = Queue()
try:
   _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon', queue,))
   _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python', queue,))
   _thread.start_new_thread(storage, (queue,))
except:
   print ('Error: unable to start threads')

while 1:
	pass
