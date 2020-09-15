import re
import requests
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 정규표현식으로 지정한 유형의 링크들을 추출하고, 그 링크사이트들의 내용을 스크랩
   ㄴ 뉴스 웹사이트(중앙일보) 메인에 보이는 모든 기사문의 제목과 내용을 스크랩

2) 각 웹사이트별로 크롤러 객체 생성
   ㄴ scraper_for_various_webpages.py, scraper_for_search_results.py 에서와 다른 구조
'''

class Content:

	def __init__(self, url, title, body):
		self.url = url
		self.title = title
		self.body = body

	def print(self):
		print('='*100)
		print('URL: {}'.format(self.url))
		print('TITLE: {}'.format(self.title))
		print('BODY:\n{}'.format(self.body))


class Website:

	def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
		self.name = name
		self.url = url
		self.targetPattern = targetPattern
		self.absoluteUrl = absoluteUrl
		self.titleTag = titleTag
		self.bodyTag = bodyTag


class Crawler:
	
	def __init__(self, site):
		self.site = site
		self.visited = []

	def getPage(self, url):
		try:
			req = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(req.text, 'html.parser')

	def safeGet(self, pageObj, selector):
		selectedElems = pageObj.select(selector)
		if len(selectedElems) > 0:
			return '\n'.join([elem.get_text() for elem in selectedElems])
		return ''

	def parse(self, url):
		bs = self.getPage(url)
		if bs is not None:
			title = self.safeGet(bs, self.site.titleTag)
			body = self.safeGet(bs, self.site.bodyTag)
			if title != '' and body != '':
				content = Content(url, title.strip(), body.strip())
				content.print()

	def crawl(self):
		"""
		Get pages from website home page
		"""
		bs = self.getPage(self.site.url)
		targetPages = bs.find_all('a', href=re.compile(self.site.targetPattern))
		for targetPage in targetPages:
			targetPage = targetPage.attrs['href']
			if targetPage not in self.visited:
				self.visited.append(targetPage)
				if not self.site.absoluteUrl:
					targetPage = '{}{}'.format(self.site.url, targetPage)
				self.parse(targetPage)


joongangilbo = Website('중앙일보', 'https://news.joins.com', '/article/', 
	True, 'h1', 'div#article_body')

# 웹사이트별로 크롤러 객체 생성
crawler = Crawler(joongangilbo)
crawler.crawl()
