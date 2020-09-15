import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

'''
*** NOTE ***

1) 다음의 MySQL 문을 실행해서 데이터베이스와 테이블을 만들 것!
	
	CREATE DATABASE wikipedia;
	
	USE wkikpedia;

	CREATE TABLE pages (
		id INT NOT NULL AUTO_INCREMENT,
		url VARCHAR(255) NOT NULL,
		created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
		PRIMARY KEY(id)
	);

	CREATE TABLE links (
		id INT NOT NULL AUTO_INCREMENT,
		fromPageId INT NULL,
		toPageId INT NULL,
		created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
		PRIMARY KEY(id)
	);

2) Kevin Bacon Game 을 테스트 하기 위한 데이터를 수집
   ㄴ 위키피디아 /wiki/Kevin_Bacon 페이지에서부터 내부 항목페이지를 따라가며 링크 수집
   ㄴ 재귀호출의 stack 수가 5를 넘지않게 조절

3) 모두 마치려면 굉장히 오랜 시간이 걸리므로, 적당한 선에서 종료할 것!

4) NLP/kevin_bacon_game_2.py 에서 후속 분석 계속!!!

5) 사용자 입력 사항
   - passwd : 로컬 서버 비밀번호 입력
'''

def insertPageIfNotExists(url):
	cur.execute('SELECT * FROM pages WHERE url = %s', (url))
	if cur.rowcount == 0:
		cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
		conn.commit()
		return cur.lastrowid
	else:
		return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
	cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', 
		(int(fromPageId), int(toPageId)))
	if cur.rowcount == 0:
		cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', 
			(int(fromPageId), int(toPageId)))
		conn.commit()


def pageHasLinks(pageId):
	cur.execute('SELECT * FROM links WHERE fromPageId = %s', (int(pageId)))
	rowcount = cur.rowcount
	if rowcount == 0:
		return False
	return True


def getLinks(pageUrl, recursionLevel):
	if recursionLevel > 4:
		return

	pageId = insertPageIfNotExists(pageUrl)
	html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
	bs = BeautifulSoup(html, 'html.parser')
	links = bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
	links = [link.attrs['href'] for link in links]

	for link in links:
		linkId = insertPageIfNotExists(link)
		insertLink(pageId, linkId)
		if not pageHasLinks(linkId):
			print("PAGE HAS NO LINKS: {}".format(link))
			getLinks(link, recursionLevel+1)


conn = pymysql.connect(
	host='127.0.0.1',
	user='root',
	passwd='',
	db='mysql'
)
cur = conn.cursor()
cur.execute('USE wikipedia')

getLinks('/wiki/Kevin_Bacon', 0) 
cur.close()
conn.close()
