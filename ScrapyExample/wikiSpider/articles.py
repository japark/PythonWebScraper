from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule

'''
*** NOTE ***

1) scrapy.Spider 가 아닌, CrawlSpider 를 상속받아 클래스 작성
   ㄴ start_urls, allowed_domains 등의 리스트 속성 제공

2) Rule 의 매개변수 4개 : link_extractor, callback, cb_kwargs, follow
   ㄴ link_extractor : 필수 매개변수이며, LinkExtractor 객체를 인자로 대입
   ㄴ callback : 페이지 내용 구문 분석
   ㄴ cb_kwargs : Callback 함수에 전달할 매개변수 딕셔너리
   ㄴ follow : 현재 링크를 향후 크롤링에 포함할지 여부
			   (default: callback 없으면 True, 있으면 False)

3) LinkExtractor 의 매개변수 2개 : allow, deny
   ㄴ allow : 정규표현식과 일치하는 링크 모두 허용
   ㄴ deny : 정규표현식과 일치하는 링크 모두 거부

4) 시행이 굉장히 오래(무한히) 지속되므로, 도중에 강제종료할 것!!!
'''

class ArticleSpider(CrawlSpider):
	name = 'articles'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
	rules = [
		Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
			callback='parse_items', follow=True,
			cb_kwargs={'is_article': True}),
		Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
			cb_kwargs={'is_article': False})
	]

	def parse_items(self, response, is_article):
		url = response.url
		print('URL is: {}'.format(url))
		title = response.css('h1::text').extract_first()
		if is_article:
			text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
			lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
			lastUpdated = lastUpdated.replace('This page was last edited on ', '')
			print('Title is: {} '.format(title))
			print('Text is: {}'.format(text))
			print('Last updated: {}'.format(lastUpdated))
		else:
			print('This is not an article: {}'.format(title))
