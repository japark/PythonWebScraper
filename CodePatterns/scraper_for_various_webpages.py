import requests
from bs4 import BeautifulSoup

'''
*** NOTE ***

1) 다양한 웹사이트에서 데이터를 추출할 때 유용한 코드 패턴
   ㄴ 추출한 데이터를 모아둘 객체 : Content
   ㄴ 웹사이트별 이름, DOM 구조에 대한 정보를 담은 객체 : Website
   ㄴ 크롤러 객체: Crawler

2) 세 가지 뉴스 웹사이트에서 각각 하나씩의 기사문을 스크랩
   ㄴ 기사의 제목, 본문을 스크랩하여 콘솔에 출력
   ㄴ 뉴스사이트마다 기사문의 제목, 본문에 대한 선택자(selector)가 다름에 유의!

3) 이런 코드 패턴을 이용하면, 후에 또다른 웹사이트가 추가되어도 쉽게 수정 가능!
   ㄴ 간편한 유지보수, 높은 확장성!!!
'''

class Content:

	def __init__(self, url, title, body):
		self.url = url
		self.title = title
		self.body = body

	def print(self):
		print('URL: {}'.format(self.url))
		print('TITLE: {}'.format(self.title))
		print('BODY:\n{}'.format(self.body))


class Website:
	""" 
	Contains information about website structure
	"""
	def __init__(self, name, url, titleTag, bodyTag):
		self.name = name
		self.url = url
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
		selectedElems = pageObj.select(selector)
		if len(selectedElems) > 0:
			return '\n'.join([elem.get_text() for elem in selectedElems])
		return ''

	def parse(self, site, url):
		"""
		Extract content from a given page URL
		"""
		bs = self.getPage(url)
		if bs is not None:
			title = self.safeGet(bs, site.titleTag)
			body = self.safeGet(bs, site.bodyTag)
			if title != '' and body != '':
				content = Content(url, title, body)
				content.print()


crawler = Crawler()

'''
또 다른 뉴스웹사이트를 추가할 땐,
그 사이트에서 사용하는 기사문 제목, 본문에 대한 선택자를 조사하여
아래 리스트에 추가해주기만 하면 된다
'''
siteData = [
	['조선일보', 'https://www.chosun.com', 'h1', 'section.article-body p'],
	['중앙일보', 'https://joongang.joins.com', 'h1', 'div#article_body'],
	['동아일보', 'https://www.donga.com', 'h1', 'div.article_txt']
]
websites = []
for row in siteData:
	websites.append(Website(row[0], row[1], row[2], row[3]))

# 크롤링 시행
print()
crawler.parse(websites[0],
	'https://www.chosun.com/national/weekend/2020/09/05/QIKBHOV47FBW5EKEVBKVHAIPFU/'
)
print('\n' + '='*100 + '\n')
crawler.parse(websites[1],
	'https://news.joins.com/article/23864478'
)
print('\n' + '='*100 + '\n')
crawler.parse(websites[2],
	'https://www.donga.com/news/Society/article/all/20200905/102800207/1'
)
