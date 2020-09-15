import requests
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 웹사이트에서 어떤 키워드에 대한 검색 결과 스크랩하기
   ㄴ O'Reilly Media 와 교보문고 에서 특정 키워드로 서적검색, 각 책의 제목과 소개글 추출

2) 검색할 웹사이트, 검색 키워드를 추가/삭제하기 용이하게 코드 구성
   ㄴ Content, Website, Crawler 클래스로 역할 구분
   ㄴ siteData, topics 리스트에 웹사이트 구조 정보, 검색 키워드를 손쉽게 추가/삭제
   ㄴ 간편한 유지보수, 높은 확장성!!!
'''

class Content:

	def __init__(self, topic, url, title, body):
		self.topic = topic
		self.title = title
		self.body = body
		self.url = url

	def print(self):
		print('='*100)
		print('New article found for topic: {}'.format(self.topic))
		print('URL: {}'.format(self.url))
		print('TITLE: {}'.format(self.title))
		print('BODY:\n{}'.format(self.body))


class Website:

	def __init__(self, name, url, searchUrl, resultListing,
		resultUrl, absoluteUrl, titleTag, bodyTag):
		self.name = name
		self.url = url
		self.searchUrl = searchUrl
		self.resultListing = resultListing
		self.resultUrl = resultUrl
		self.absoluteUrl = absoluteUrl
		self.titleTag = titleTag
		self.bodyTag = bodyTag


class Crawler:

	def getPage(self, url):
		try:
			req = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(req.text, 'html.parser')

	def safeGet(self, pageObj, selector):
		childObj = pageObj.select(selector)
		if len(childObj) > 0:
			return childObj[0].get_text()
		return ''

	def search(self, topic, site):
		"""
		Searches a given website for a given topic and records all pages found
		"""
		bs = self.getPage(site.searchUrl + topic)
		searchResults = bs.select(site.resultListing)
		for result in searchResults:
			url = result.select(site.resultUrl)[0].attrs['href']
			# Check to see whether it's a relative or an absolute URL
			if(site.absoluteUrl):
				bs = self.getPage(url)
			else:
				bs = self.getPage(site.url + url)
			if bs is None:
				print('Something was wrong with that page or URL. Skipping!')
				return
			title = self.safeGet(bs, site.titleTag)
			body = self.safeGet(bs, site.bodyTag)
			if title != '' and body != '':
				content = Content(topic, url, title.strip(), body.strip())
				content.print()


crawler = Crawler()

siteData = [
	['O\'Reilly Media', 'https://www.oreilly.com/', 'https://ssearch.oreilly.com/?q=',
		'article.product-result', 'p.title a', True, 'h1', 'div.product-description'],
	['교보문고', 'http://www.kyobobook.co.kr',
		'https://search.kyobobook.co.kr/web/search?vPstrKeyWord=',
		'tbody#search_list tr', 'div.title a', True, 'h1.title strong',
		'div.box_detail_article'],
]
sites = []
for row in siteData:
	sites.append(Website(row[0], row[1], row[2],
						 row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
	print('GETTING INFO ABOUT: ' + topic)
	for targetSite in sites:
		crawler.search(topic, targetSite)
