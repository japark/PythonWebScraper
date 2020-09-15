import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

'''
*** NOTE ***

1) Wikipedia 에서 특정 주제(여기서는 Napoleon)에 관한 페이지에서 시작해서,
   내부 링크를 따라가면서 각 페이지의 제목(title)과 첫 문단(content)을 데이터베이스에 저장

2) 무한히 동작하는 코드이므로 적당한 선에서 프로그램 정지시킬 것!!!

3) 사용자 입력 사항
   - <database name> : 데이터베이스 이름을 입력
   - <table name> : 선택된 데이터베이스 안의 테이블 이름을 입력
   - passwd : 로컬 서버 비밀번호 입력
'''

def store(title, content):
	cur.execute(
		'INSERT INTO <table name> (title, content) VALUES ("%s", "%s")',
		(title, content)
	)
	cur.connection.commit()


def getLinks(articleUrl):
	html = urlopen('http://en.wikipedia.org'+articleUrl)
	bs = BeautifulSoup(html, 'html.parser')
	title = bs.find('h1').get_text()
	contents = bs.find('div', {'id':'mw-content-text'}).find_all('p')
	for content in contents:
		if content.get_text().strip(): break
	content = content.get_text().strip()
	store(title, content)
	return bs.find('div', {'id':'bodyContent'}).find_all('a',
		href=re.compile('^(/wiki/)((?!:).)*$'))


conn = pymysql.connect(
	host='127.0.0.1',
	user='root',
	passwd='',
	db='mysql'
)
cur = conn.cursor()
cur.execute('USE <database name>')

random.seed(datetime.datetime.now())

links = getLinks('/wiki/Napoleon')
try:
	while len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs['href']
		print(newArticle)
		links = getLinks(newArticle)
finally:
	cur.close()
	conn.close()
