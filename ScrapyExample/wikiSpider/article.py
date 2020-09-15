import scrapy

'''
*** NOTE ***

1) 가장 기본적인 스파이더 작성
   ㄴ 지정한 웹페이지들에 대해서 스크래핑

2) 콘솔 실행문 : scrapy runspider article.py
'''

class ArticleSpider(scrapy.Spider):
	name = 'article'

	def start_requests(self):
		urls = [
			"https://en.wikipedia.org/wiki/Python_%28programming_language%29",
			"https://en.wikipedia.org/wiki/Functional_programming",
			"https://en.wikipedia.org/wiki/Monty_Python"
		]
		return [scrapy.Request(url=url, callback=self.parse) for url in urls]

	def parse(self, response):
		url = response.url
		title = response.css('h1::text').extract_first()
		print('URL is: {}'.format(url))
		print('Title is: {}'.format(title))
